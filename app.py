from flask import Flask, render_template, redirect, url_for, jsonify
from api_fetch import harvest, manipulate
from model_train import trainer_DL, trainer_RF
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

@app.route("/decision/<mine>")
def popin(mine="Gold"):
    mine = mine.capitalize()
    return render_template("data.html",into=mine)

@app.route("/tableinfo/<dollars>")
def money(dollars="Gold"):
    data_dl = read_csv(f"data/csv/{dollars}_DL_FinalTable.csv",index_col=0)
    data_rf = read_csv(f"data/csv/{dollars}_FinalTable_RF.csv",index_col=0)
    data_dl = data_dl.fillna("Missing")
    data_rf = data_rf.fillna("Missing")
    data_dl = data_dl.to_dict("split")
    data_rf = data_rf.to_dict("split")
    del data_dl["index"]
    del data_rf["index"]
    combined = {"DL":data_dl,"RF":data_rf}
    return jsonify(combined)

@app.route("/update/<which>")
def new_info(which="a"):
    harvest(which)
    return redirect(url_for("home"))

@app.route("/manip")
def manip_info():
    manipulate()
    return redirect(url_for("home"))

@app.route("/predict_DL")
def crystal_ball():
    trainer_DL()
    return redirect(url_for("home"))

@app.route("/predict_RF")
def quartz_ball():
    trainer_RF()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)