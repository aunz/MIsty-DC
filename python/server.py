#!/usr/bin/env python
from flask import Flask, request
import pandas as pd

from model import model, processData


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'You should go to /predict'

@app.route('/predict', methods=['post'])
def route_predict():
    query = request.get_json(force=True)
    print('Received:', query)
    for x in range(1, 27):
        x = 'x' + str(x)
        if x not in query: return ''

    data = pd.DataFrame(query)
    data = processData(data)
    prediction = model.predict(data)
    print('Prediction done', prediction)
    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True, port=5555)