import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import MedicalInsurence

app = Flask(__name__)

#########################################################################
####################### Prediction API  #################################
#########################################################################

@app.route('/predict_charges',methods = ['POST','GET'])
def get_insurence_charges():
    print("We are using POST method")
    data = request.form
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
    med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
    charges = med_ins.get_predicted_charges()

    return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=True)
