import pandas as pd
import cPickle
from flask import jsonify, request, Flask

app = flask.Flask(__name__)

df = cPickle.load(open('assets/big_df_model-ready.p', 'rb'))

def TheRecommender(df, cuisine, stars, max_price):
    if stars == 0:
        xx = df[(df['cuisine'] == cuisine) & (df['bib'] == 1) & \
               (df['avg_USD'] <= max_price)].sort_values(by = 'adj_standing', \
                ascending = False)[['name', 'cuisine', 'blurb', 'avg_USD', \
                'stars', 'bib']]
        yy = df[(df['cuisine'] == cuisine) & (df['included'] == 0) & \
            (df['avg_USD'] <= max_price)].sort_values(by = 'adj_standing', \
            ascending = False)[['name', 'cuisine', 'blurb', 'avg_USD', \
            'stars', 'bib']]
        z = pd.concat([x, y], axis = 0)
        return z.iloc[0]['name']
    else:
        xx = df[(df['cuisine'] == cuisine) & (df['stars'] == stars) & \
               (df['avg_USD'] <= max_price)].sort_values(by = 'adj_standing', \
                ascending = False)[['name', 'cuisine', 'blurb', 'avg_USD', \
                'stars', 'bib']]
        return x.iloc[0]['name']

@app.route('/page')
def page():
   with open("templates/page.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    print 'Starting recommendation session'
    if flask.request.method == 'POST':
        print 'POST RECEIVED'
        inputs = flask.request.form
        print 'INPUTS FORM'
        cuisine = inputs['cuisine'][0]
        stars = inputs['stars'][0]
        max_price = inputs['max_price'][0]

        allrecs = TheRecommender(df, cuisine, stars, max_price)
        rec = {'restaurant name' : allrecs}
        # results = {'name': allrecs.iloc[0]['name']}
        return flask.jsonify(rec)


if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = int('4000')
    app.run(HOST, PORT)
