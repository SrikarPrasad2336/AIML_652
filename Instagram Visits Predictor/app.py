from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import pandas as pd
import os

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Load the CSV file
data = pd.read_csv('instagram_visits_prediction_large.csv')

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        follower_count = float(request.form.get('follower_count', 0))
        hashtags_count = int(request.form.get('hashtags_count', 0))
        caption_length = int(request.form.get('caption_length', 0))
        avg_likes = float(request.form.get('avg_likes', 0))
        avg_comments = float(request.form.get('avg_comments', 0))
        post_type = int(request.form.get('post_type', 0))
        time_of_day = int(request.form.get('time_of_day', 0))
    except ValueError:
        return "Invalid input! Please enter numbers only.", 400  # HTTP 400 Bad Request

    # Predict using the model
    features = np.array([[follower_count, hashtags_count, caption_length, avg_likes, avg_comments, post_type, time_of_day]])
    result = model.predict(features)[0]

    # Categorize the prediction into High, Medium, or Low
    if result > 15000:
        prediction_category = "High"
    elif result > 5000:
        prediction_category = "Medium"
    else:
        prediction_category = "Low"

    return render_template('index.html', result=f'Predicted Visits: {prediction_category}')

@app.route('/data')
def show_data():
    return data.head(20).to_html()  # Display first 20 rows as an HTML table

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


