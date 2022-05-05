import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('modelo_udg.pkl', 'rb')) # loading the trained model

@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    CALENDARIO = request.form['CALENDARIO']
    PUNTAJE_MINIMO = request.form['PUNTAJE_MINIMO']
    CUPO = request.form['CUPO']
    ADMITIDOS = request.form['ADMITIDOS']
    ASPIRANTES = request.form['ASPIRANTES']
    # retrieving values from form
    input_variables = pd.DataFrame([[CALENDARIO, PUNTAJE_MINIMO, CUPO, ADMITIDOS, ASPIRANTES]],
                                        columns=['CALENDARIO', 'PUNTAJE_MINIMO', 'CUPO', 'ADMITIDOS', 'ASPIRANTES'],
                                        dtype=float,
                                        index=['input'])

    prediction = model.predict(input_variables)[0] # making prediction

    #if statement to determine if the probability is high or low according to the prediction result
    if prediction == 0:
        result = 'Probabilidad baja'
    elif prediction == 1:
        result = 'Probabilidad alta'

    return render_template('index.html', prediction_text=result) # rendering the predicted result on the page


if __name__ == "__main__":
    app.run(debug=True)