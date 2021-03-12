import numpy as np
import pickle
from flask import Flask,request,render_template

#Load ML Model
model = pickle.load(open('model.pkl','rb'))

#create application
app = Flask(__name__)

#Bind home function to URL
@app.route('/')
def home():
    return render_template('heart.html')

#Bind predict function to URL
@app.route('/predict',methods=['POST'])
def predict():
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)

    output = prediction

    #check the output and retrive the result with html tag based on the values
    if output == 1:
        return render_template('heart.html',
        result = "Congratulations, you're not likely to have Heart Disease!")
    else:
        return render_template('heart.html',
        result = "You may have Heart disease,Please consult a doctor!")
if __name__ == '__main__':
#Run application
    app.run()
