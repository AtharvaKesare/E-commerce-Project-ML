E-Commerce Product Recommendation System
A simple, interactive web app that recommends similar products based on customer reviews, built with Streamlit and basic machine learning.

Features
Suggests similar products when a user selects a product.

Recommendations are always for the same type (e.g., phones for phones, fridges for fridges), not unrelated items.

Uses customer review text and basic machine learning (TF-IDF, cosine similarity).

Interactive web interface for easy demo and use.

Demo
<img width="1067" height="887" alt="image" src="https://github.com/user-attachments/assets/aac67656-eb6c-4313-8e9a-f2ca4fdf8b83" />

<img width="1103" height="866" alt="image" src="https://github.com/user-attachments/assets/44be16d7-911e-4f78-84b0-68c2769f1fcc" />



How It Works
Choose a product: The user selects an item from the dropdown.

Review processing: The app converts review texts into vectors using TF-IDF.

Similarity check: Cosine similarity finds the most similar reviews and products.

Strict filtering: Only recommends products of the same type as selected (using keywords).

Results shown: Top 5 relevant items displayed with their details.

Tech Stack & Libraries
Python

pandas (for data handling)

scikit-learn (TF-IDF and cosine similarity)

Streamlit (web app UI)

Getting Started
Clone this repo:

bash
git clone https://github.com/yourusername/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
Install requirements:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
Open your browser to the Streamlit link to interact.

Dataset
The sample product review dataset is included as ecommerce_reviews_clean.csv.

Project Structure
text
|-- app.py            # Main Streamlit web app
|-- ecommerce_reviews_clean.csv   # Preprocessed dataset
|-- requirements.txt  # Dependencies
|-- README.md         # Project documentation
Future Improvements
Add collaborative filtering for personalized suggestions.

Use advanced models (e.g., BERT, embeddings) for deeper text analysis.

Add user authentication or a "buy" link.
