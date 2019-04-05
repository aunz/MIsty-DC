# Misty Data Challenge
Predict the binary target *y* (0 or 1) given features *X* 
---

### Data

- The data has 10,000 rows
- There are 26 features, ~ 11 are categorical
- The data are highly imbalanced, with ~1% only in class 1
- [EDA](training/Misty_EDA.ipynb)

### Model
- The model was trained using Scikit-learn API and saved into pickle format
- The final model consists of an ensemble of logistic regression, xgboost and naive bayes

### Deployment
- The model is deployed using Flask
- Nodejs is used in front of Flask to validate inputs

How to run? Docker or manual installation.

# Docker

`docker run -d -p 3000:3000 aunz10/misty-dc`

# Manual installation

- Install [nodejs](https://nodejs.org/), v11.13.0
- Install [python3](https://www.python.org/downloads/), minimum v3.6
- Install [pandas](http://pandas.pydata.org/pandas-docs/stable/install.html), v0.24
- Install [scikit-learn](https://scikit-learn.org/stable/install.html), v0.20. This installation will also install its dependency such as numpy
- Install [xgboost](https://xgboost.readthedocs.io/en/latest/build.html), v0.82
- Install [Flask](http://flask.pocoo.org/docs/1.0/installation/) v1.0 


### Express server
under the main folder, run

`node node\index.js`

This will create an express server listening on port 3000


### Flask server
under the main folder, run

`python3 python\server.py`

This will create a Flask server listening on port 5555

# Give it a try

Issue a get request

`curl "localhost:3000/predict?x1=id82386&x2=8.1.0&x3=LGE_LM-V405&x4=US&x5=0&x6=1999&x7=19&x8=0&x9=2&x10=1&x11=0&x12=0.1320754717&x13=0&x14=53&x15=LGE&x16=0&x17=8&x18=0&x19=0&x20=0&x21=1&x22=0&x23=TRUE&x24=492786776143062000&x25=Facebook&x26="`

You should get a 200 json response `{ prediction: int{0|1} }`

- If one of the variables is not provided, it will return a 400 status
- If one the the variable type is not correct, it will also return a 400 status. For example, x7 should be a number, if x7=abc, the server will return a 400