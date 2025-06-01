A simple machine learning web app that predicts whether you should play basketball based on weather conditions. It uses a Gaussian Naive Bayes classifier and offers both command-line and web interface prediction options.

Project Structure

- temperature.csv         # Dataset with weather conditions and outcomes
- train_model.py          # Script to train and save the ML model
- predict.py              # Script to load the model and make predictions
- model.pkl               # Pickled trained model and label encoders
  index.html              # Web UI for prediction (requires PHP)


How It Works

.Training

The train_model.py script loads temperature.csv.

Categorical features are encoded using LabelEncoder.

A Gaussian Naive Bayes classifier is trained on the features.

The model and encoders are saved in model.pkl.

.Prediction

predict.py loads the model and encoders.

Takes inputs either via:

sys.argv (for command-line use), or

Dictionary (for integration with web UI).

Outputs "Yes" or "No" for playing basketball.

.Web Interface

A basic HTML+PHP form allows user input via dropdowns.

The PHP script passes user inputs to the Python model.

The result is shown on the webpage.

How to Use

Train the Model
bash
Copy
Edit
python train_model.py
Make sure temperature.csv is in the same directory.

Make Predictions via Command Line
bash
Copy
Edit
python predict.py Sunny Hot High False
Outputs: Yes or No

Run Web Interface
Ensure PHP is installed on your server or localhost.

Place all files (index.html, predict.py, model.pkl) in your web directory.

Visit the HTML form in your browser.

Submit the weather conditions to get a prediction.


Dependencies

Python 3.x
pandas
scikit-learn


Notes

Ensure the model.pkl file is in the same directory as predict.py and your web interface.
This project is ideal for learning ML pipelines, encoding, and deploying basic models.
