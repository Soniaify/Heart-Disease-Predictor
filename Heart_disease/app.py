from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('Heart_disease/heart_model.pkl')  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form.get(key)) for key in request.form.keys()]
    prediction = model.predict([features])[0]
    return render_template('index.html', prediction=prediction)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
