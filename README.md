How to Run the Application Follow these steps to set up and run the project on your local machine.

Prerequisites You must have Python 3.8 or a newer version installed. It is recommended to use a virtual environment.

Clone the repository git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git cd YOUR_REPOSITORY_NAME

Install Dependencies Install the required Python libraries using pip.

pip install -r requirements.txt

Run the Application Start the Flask development server.
python app.py

The application will be running at http://127.0.0.1:5000/. Open this URL in your web browser to use the fake news detector.

File Structure app.py: The main Flask application file. It handles the web routes and integrates the machine learning model.

model.py: Contains the logic for training and saving the machine learning model. It is called by app.py.

templates/: Contains the HTML files for the web interface.

index.html: The main page with the form for user input.

dataset/: Holds the dataset used for training the model.

Fake.csv: Contains fake news articles.

True.csv: Contains real news articles.

requirements.txt: Lists all the Python libraries required for the project.

.gitignore: Tells Git to ignore unnecessary files like Python cache files and serialized model files.
