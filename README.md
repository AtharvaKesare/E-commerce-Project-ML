# E-Commerce Product Recommendation System

**A simple, interactive web app that recommends similar products based on customer reviews, built with Streamlit and basic machine learning.**

---

## Features

- Suggests similar products when a user selects a product.
- Recommendations are always for the same type (e.g., phones for phones, fridges for fridges), not unrelated items.
- Uses customer review text and basic machine learning (TF-IDF, cosine similarity).
- Interactive web interface for easy demo and use.

---

## Demo

<img width="1067" height="887" alt="image" src="https://github.com/user-attachments/assets/9b46bb7b-c2d1-477a-b815-e1ef422767d2" />

<img width="1103" height="866" alt="image" src="https://github.com/user-attachments/assets/9b86a87a-8c2c-4252-91ed-36385444f722" />


---

## How It Works

1. **Choose a product:** The user selects an item from the dropdown.
2. **Review processing:** The app converts review texts into vectors using TF-IDF.
3. **Similarity check:** Cosine similarity finds the most similar reviews and products.
4. **Strict filtering:** Only recommends products of the same type as selected (using keywords).
5. **Results shown:** Top 5 relevant items displayed with their details.

---

## Tech Stack & Libraries

- **Python**
- **pandas** (for data handling)
- **scikit-learn** (TF-IDF and cosine similarity)
- **Streamlit** (web app UI)

---

## Getting Started

1. Clone this repo:
    ```
    git clone https://github.com/yourusername/ecommerce-recommendation-system.git
    cd ecommerce-recommendation-system
    ```
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    streamlit run app.py
    ```
4. Open your browser to the Streamlit link to interact.

---

## Dataset

- The sample product review dataset is included as `ecommerce_reviews_clean.csv`.

---

## Project Structure

