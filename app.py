#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
from joblib import dump, load

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
path = os.getcwd()

def get_predictions(req_model, features):
    return load(f'Models/{req_model}.joblib').predict(features)[0]


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['Age']
        sex = request.form['Sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        req_model = request.form['req_model']

        features = [float(feature) for feature in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        target = get_predictions(req_model, [features])

        if target==1:
            sale_making = 'Patient has a heart disease probably'
        else:
            sale_making = 'Patient does not have a heart disease probably'

        return render_template('home.html', target = target, sale_making = sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)