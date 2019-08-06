from flask import Flask, render_template, redirect, url_for, jsonify
from api_fetch import harvest, manipulate
from model_train import trainer
from pandas import read_csv

app = Flask(__name__)

# Setting up routes to rule the world
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/moneymaker")
def giveaction():
    which = ["Gold","Silver","Platinum","Palladium"]
    container = []
    for check in which:
        strength = 0
        strength = read_csv(f"data/csv/{check}_DL_FinalTable.csv")["Signal"][0]
        strength += .5*read_csv(f"data/csv/{check}_FinalTable_RF.csv")["Signal"][0]
        container.append(strength)
    return jsonify(container)

@app.route("/update/<which>")
def new_info(which="a"):
    harvest(which)
    return redirect(url_for("home"))

@app.route("/manip")
def manip_info():
    manipulate()
    return redirect(url_for("home"))

@app.route("/predict")
def crystal_ball():
    trainer()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)