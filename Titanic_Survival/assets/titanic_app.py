import flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

#-------- MODEL GOES HERE -----------#
import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing

titanic = pd.read_csv('titanic_final.csv')
preX = titanic[[u'SibSp', u'class_3', u'title_Mr']]

X = pd.DataFrame(preprocessing.scale(preX), columns = preX.columns)

y = titanic['Survived']

PREDICTOR = linear_model.LogisticRegression(C=1, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=-1,
          penalty='l1', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False).fit(X, y)

#-------- ROUTES GO HERE -----------#
from flask import jsonify
@app.route('/predict', methods=["GET"])
def predict():
    class_3 = flask.request.args['class_3']
    title_Mr = flask.request.args['title_Mr']
    sibsp = flask.request.args['SibSp']

    item = [class_3, title_Mr, SibSp]
    score = PREDICTOR.predict_proba(item).T
    results = {'survival chances': score[0,1], 'death chances': score[0,0]}
    return flask.jsonify(results)

@app.route('/page')
def page():
   with open("page.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

       inputs = flask.request.form

       pclass = inputs['pclass'][0]
       sex = inputs['sex'][0]
       age = inputs['age'][0]
       fare = inputs['fare'][0]
       sibsp = inputs['sibsp'][0]

       item = [pclass, sex, age, fare, sibsp]
       score = PREDICTOR.predict_proba(item)
       results = {'survival chances': score[0,1], 'death chances': score[0,0]}
       return flask.jsonify(results)

if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = 4000
    app.run(HOST, PORT)
