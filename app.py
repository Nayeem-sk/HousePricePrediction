import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def predict_data():
    '''
    For rendering results on HTML GUI
    '''
    output = 0
    values = []
    if request.method == 'POST':
        area = int(request.form['area'])
        floor = int(request.form['floor'])
        values.append(area)
        values.append(floor)
        output = model.predict([values])
    return render_template('index.html', prediction_text='House price is $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)