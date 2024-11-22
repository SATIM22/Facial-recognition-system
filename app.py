from flask import Flask, render_template, request
#import cv2
import numpy as np
#from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=[])
def result():
    return render_template('result.html')
if __name__ == "__main__":
    app.run(debug=True)