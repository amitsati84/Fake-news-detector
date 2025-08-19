import joblib
from flask import Flask, request, render_template

# We now import our machine learning functions from the separate model.py file.
from model import predict_news, load_model

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')

# Global list to store prediction history
prediction_history = []

# Load the trained model and vectorizer when the app starts.
# This ensures we don't reload them on every request.
# The `load_model()` function will handle training if the files don't exist.
vectorizer, model = load_model()

# Define the main route for the home page.
@app.route('/')
def home():
    """
    Renders the home page of the web application.
    Flask will automatically look for 'index.html' inside the 'templates' folder.
    """
    return render_template('index.html', prediction_history=prediction_history)

# Define the prediction route.
@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles prediction requests by getting the text from the form,
    making a prediction using the model, and displaying the result.
    """
    # Get the text from the form
    user_text = request.form['text']

    # Use the function from model.py to get the prediction.
    result = predict_news(user_text, vectorizer, model)

    # Save the prediction and original text to the history list
    prediction_history.insert(0, {'text': user_text, 'prediction': result})
    
    # Render the template with the prediction result and history
    return render_template('index.html', 
                           prediction_result=result, 
                           prediction_history=prediction_history, 
                           user_text=user_text)

# --- Main execution block ---
if __name__ == '__main__':
    print("Starting the Flask web application...")
    print("The web app will be available at http://127.0.0.1:5001")
    # You will now see two lines of output in the terminal:
    # 1. "Model loaded/trained successfully." (from model.py)
    # 2. "Running on http://127.0.0.1:5001" (from Flask)
    app.run(debug=True, port=5001)