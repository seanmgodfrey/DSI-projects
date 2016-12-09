import flask
import pandas as pd
import cPickle

app = flask.Flask(__name__)

# from cuisinify import cuisinify
# import seaborn as sns
# from IPython.display import Image
# from IPython.core.display import HTML
# import spacy
# import os
# from spacy.en import English
# from matplotlib import gridspec
# from matplotlib import cm
# from sklearn.cross_validation import KFold, cross_val_score, train_test_split
# from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, \
#     ExtraTreesClassifier, ExtraTreesRegressor
# from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor
# from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
# from sklearn.metrics import confusion_matrix, recall_score, precision_score, accuracy_score, \
#     roc_auc_score, roc_curve
# from sklearn.metrics import classification_report
# import matplotlib.patheffects as path_effects
# from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
# from scipy.stats import randint
# import time
# from operator import itemgetter

df = cPickle.load(open('assets/big_df_model-ready.p', 'rb'))

def TheRecommender(df, cuisine, distinction, max_price, \
                                sort_by = 'adj_standing', ascending = False):
    if distinction == 0:
        x = df[(df['cuisine'] == cuisine) & (df['bib'] == 1) & \
            (df['avg_USD'] >= min_price) & (df['avg_USD'] <= max_price)].\
            sort(sort_by, ascending = ascending)[['name', 'cuisine', 'blurb', \
            'avg_USD', 'stars', 'bib']]
        y = df[(df['cuisine'] == cuisine) & (df['included'] == 1) & \
            (df['avg_USD'] <= max_price)].sort(sort_by, ascending = ascending)\
            [['name', 'cuisine', 'blurb', 'avg_USD', 'stars', 'bib']]
        z = pd.concat([x, y], axis = 0)
        return z
    else:
        x = df[(df['cuisine'] == cuisine) & (df['stars'] == distinction) & \
            (df['avg_USD'] <= max_price)].sort(sort_by, ascending = ascending)\
            [['name', 'cuisine', 'blurb', 'avg_USD', 'stars', 'bib']]
        return x

@app.route('/page')
def page():
   with open("page.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

       inputs = flask.request.form

       cuisine = inputs['cuisine'][0]
       distinction = inputs['distinction'][0]
       max_price = inputs['max_price'][0]


       results = TheRecommender(df, cuisine, distinction, max_price, \
            sort_by = 'adj_standing', ascending = False)

       return flask.jsonify(results)

if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
