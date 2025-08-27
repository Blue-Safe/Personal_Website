from flask import Flask, render_template

app = Flask(__name__)  # Initialize Flask app

@app.route("/")  # Home page route
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development