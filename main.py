# stages of developing machine learning model:

# 1) data cleaning or data analysing by exploratory data analysis or feature engineering.

# 2) developing model through the cleaned data and applying if necessary algorithm.

# 3) creating flask app and combining of pickle file with them.

# 4) deployment of model in cloud platform.

# flaskapp creation: 

from flask import Flask

from flask import render_template,url_for

from flask import *

import numpy as np

import pickle


app=Flask(__name__,template_folder='templates')
model=pickle.load(open('model.pkl','rb')) # in this line we are importing pickle file which we have stored and opening it as rb.(read binary)

# to access our code we doesnt need to use py or ipynb we can directly use pkl file of an code.

@app.route("/")

def home():
    return render_template('index.html')



@app.route("/predict",methods=['POST'])

def predict():

    features=[int(x) for x in request.form.values()] # in this line we are creating a int variable x and we are iterating contents with the help of for loop by request method on flask.

    final_features=[np.array(features)] # here we are storing our features as array inside variable named final_features.

    prediction=model.predict(final_features) # in this line we are using model because we stored our python file inside pickle module.

    output=round(prediction[0],2) # here inside prediction we give [0] it takes the output in round manner and next 2 we gave for the print of decimal number after decimal ends.

    # above round function gives the decimal output in the limit way possible.

    return render_template('index.html',prediction_text="the salary of an employee is {}".format(output))

    # in the above line we are once again taking the predicted value to the same page named index.html .

# model deployment:

# to deploy a model in heroku we need to create procfile:

# which includes application type,server info and at the last we need to enter name of the file. 

# here application type- web
# server info-gunicorn
# filename-app

#  inside the procfile we need to enter the referred syntax:  web:gunicorn app:app


if __name__=="__main__":
    app.run(debug=True)