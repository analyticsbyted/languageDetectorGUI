from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open('models/trained_pipeline-0.1.0.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect_language():
    text = [str(x) for x in request.form.values()] request.form.get("text")
    # Perform language detection logic here
    # Call the FastAPI backend or use your existing code
    
    # Return the detected language as a response
    return f"The detected language is: <strong>English</strong>"  # Replace with actual detected language

if __name__ == "__main__":
    app.run(debug=True)

