# app.py

from flask import Flask, request, render_template
from google.cloud import aiplatform
from dotenv import load_dotenv
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
load_dotenv()

# Initialize GCP AI Platform

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/mohdyusuf325/Downloads/majorproject-423008-545b126fcf7d.json"

aiplatform.init(project="mtp-yusuf", location="us-central1")
endpoint = aiplatform.Endpoint("5334924975969140736")

def predict_instances(instances):
    # Make predictions
    prediction = endpoint.predict(instances=instances)
    return prediction

flower_image_mapping = {
    "Iris-setosa": "static/iris-setosa.jpeg",
    "Iris-versicolor": "static/iris-versicolor.jpeg",
    "Iris-virginica": "static/iris-virginica.jpeg"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from form

        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Prepare instance data
        instances = [[sepal_length, sepal_width, petal_length, petal_width]]
        #data = request.form.get("data")

        # Process data (e.g., convert to list of floats)
        #instances = [[float(val) for val in data.split(",")]]
        
        # Get prediction
        prediction = predict_instances(instances)
        predicted_flower_name = prediction.predictions[0] 
        predicted_flower_image_path = flower_image_mapping.get(predicted_flower_name, "default.jpg") 

        data = {
            "predicted_flower_name": predicted_flower_name,
            "predicted_flower_image_path": predicted_flower_image_path,
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        return render_template("index.html", data=data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
