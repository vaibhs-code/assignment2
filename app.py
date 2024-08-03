from flask import Flask, redirect, url_for, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)
loaded_model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

def WeightPredictor(height):
    result = loaded_model.predict([[height]])
    return "Predicted Weight is " + str(result[0][0]) + "kg"

# Uncomment Lines To use HTML 

# def WeightPredictor_value(height):
#     result = loaded_model.predict([[height]])
#     return str(result[0][0])

@app.route("/results", methods=["POST"])
def output():
    h = int(request.form['h'])
    #return render_template("result.html", height=h, weight= WeightPredictor_value(h))
    return WeightPredictor(h) # COMMENT THIS IF THE ABOVE LINE IS NOT COMMENTED

# REST API
@app.route("/predict", methods=["POST"])
def predict():
    json_ = request.json
    data = json_[0]
    output = []
    for i in range(len(json_)):
        prediction = loaded_model.predict([[json_[i]["height"]]])
        output.append(prediction[0][0])
    return jsonify(Predictions = output,status = 200, mimetype = 'application/json')


if __name__ == "__main__":
    app.run()