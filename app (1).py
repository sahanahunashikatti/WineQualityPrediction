from xml.sax.handler import feature_external_ges
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
#Creation of Flask
app = Flask(__name__)

#loading the pickle model
model = pickle.load(open('wine_pkl.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods =['POST'])
def predict():
    data1=request.form['a']
    data2=request.form['b']
    data3=request.form['c']
    data4=request.form['d']
    data5=request.form['e']
    data6=request.form['f']
    data7=request.form['g']
    data8=request.form['h']
    data9=request.form['i']
    data10=request.form['j']
    data11=request.form['k']
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11]])
    pred=model.predict(arr)
    return render_template('after.html', dataq=pred)
   # float_features = [float(x) for x in request.form.values()]
    #features = [np.array(float_features)]
    #prediction = model.predict(features)

   # return render_template("home.html", prediction_test = "The wine is {}".format(prediction))
if __name__ =="__main__":
    app.run(debug=True)