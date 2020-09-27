# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:01:53 2020

@author: ujwal
"""

from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

pickle_in = open("svm_cancer_prediction.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """
    For taking input
    """
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction=classifier.predict(final_features)
    if prediction[0] == 2:
        pred="Benign"
    else:
        pred="Malignant"
    return render_template("index.html", prediction_text = "The suspected cell maybe {}".format(pred))


if __name__=="__main__":
    app.run()