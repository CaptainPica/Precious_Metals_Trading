from flask import Flask, render_template

app = Flask(__name__)

# Setting up routes to rule the world
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)