import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r"D:\ML E-commerce Project\ecommerce_reviews_clean.csv")
        return df
    except Exception as e:
        st.error(f"Could not load CSV file: {e}")
        return None

df = load_data()

if df is None:
    st.stop()

st.title("🛒 E-Commerce Product Recommendation System")
st.write("Based on Customer Reviews")

product_list = df['Product_Name'].unique()
selected_product = st.selectbox("Select a Product:", product_list)

if selected_product:
    # Get selected's category
    selected_cat = df[df['Product_Name'] == selected_product]['Category'].values[0]
    filtered_df = df[df['Category'] == selected_cat].copy()

    # OPTIONAL: Filter for only similar product types using keywords
    phone_keywords = ['phone', 'mobile', 'galaxy', 'iphone']
    if any(kw in selected_product.lower() for kw in phone_keywords):
        mask = filtered_df['Product_Name'].str.lower().str.contains('|'.join(phone_keywords))
        if mask.sum() > 1:
            filtered_df = filtered_df[mask]
    
    # Remove duplicate products (keep the best-rated review)
    filtered_df = filtered_df.sort_values(by="Rating", ascending=False)
    filtered_df = filtered_df.drop_duplicates(subset='Product_Name')
    filtered_df = filtered_df.reset_index(drop=True)
    
    # Check if the selected product is present after filtering
    if selected_product not in filtered_df['Product_Name'].values:
        st.warning("No results found for the selected product after keyword refinement. Try another product.")
        st.stop()

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(filtered_df['Review_Text'])
    
    # Find the new index
    idx = filtered_df[filtered_df['Product_Name'] == selected_product].index[0]

    # Similarity scores
    cos_sim = cosine_similarity(tfidf_matrix)
    sim_scores = list(enumerate(cos_sim[idx]))
    # Sort by similarity score, skip itself
    sim_scores = [score for score in sim_scores if score[0] != idx]
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    if not sim_scores:
        st.warning("Not enough similar products to recommend.")
    else:
        # Get top 5 unique recommendations
        rec_indices = [i[0] for i in sim_scores[:5]]
        top_recommendations = filtered_df.iloc[rec_indices]
        st.success(f"Top 5 Recommended Products similar to **{selected_product}** (Category: {selected_cat}):")

        for _, product in top_recommendations.iterrows():
            with st.expander(f"🛍️ {product['Product_Name']}"):
                st.write(f"**Brand:** {product['Brand']}")
                st.write(f"**Category:** {product['Category']}")
                st.write(f"**Rating:** {product['Rating']}")
                st.write(f"**Review:** {product['Review_Text']}")
                st.write(f"**Sentiment:** {product['Sentiment']}")
                st.write(f"**Helpful Votes:** {product['Helpful_Votes']}")

        # Optional download button
        if st.button("📥 Download Recommendations"):
            csv = top_recommendations.to_csv(index=False).encode('utf-8')
            st.download_button(label="Download CSV", data=csv, file_name='recommendations.csv', mime='text/csv')
