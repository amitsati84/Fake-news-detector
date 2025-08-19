import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import os
import re
import string

# --- Define data cleaning function ---
def clean_text(text):
    """
    Cleans the input text by removing unwanted characters and converting to lowercase.
    Args:
        text (str): The text to clean.
    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\\W"," ",text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# --- Function to load the model (or train it if it doesn't exist) ---
def load_model():
    """
    Loads the saved model and vectorizer.
    This is for Vercel deployment where the files are already in the repo.
    Returns:
        tuple: A tuple containing the loaded vectorizer and model.
    """
    # Load the model files directly, assuming they exist in the root directory
    print("Loading saved model from repository...")
    try:
        vectorizer = joblib.load('vectorizer.pkl')
        model = joblib.load('model.pkl')
        print("Model and vectorizer loaded successfully.")
        return vectorizer, model
    except FileNotFoundError:
        print("Error: Model files not found. Make sure vectorizer.pkl and model.pkl are in the root directory.")
        # We exit here because without the model files, the app cannot run.
        exit()

# --- Function to make a prediction ---
def predict_news(text, vectorizer, model):
    """
    Takes a news article text, preprocesses it, and returns the prediction.
    """
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return "Fake News" if prediction[0] == 1 else "Real News"