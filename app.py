from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect_language():
    text = request.form.get("text")
    # Perform language detection logic here
    # Call the FastAPI backend or use your existing code
    
    # Return the detected language as a response
    return f"The detected language is: <strong>English</strong>"  # Replace with actual detected language

if __name__ == "__main__":
    app.run(debug=True)

