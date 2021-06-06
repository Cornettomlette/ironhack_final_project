#!/usr/bin/python
# -*- coding: utf-8 -*-


import flask
from patient_prediction import *


from flask import render_template
from flask import request

# Initialize web server

app = flask.Flask(__name__)
app.config['DEBUG'] = True



# This API returns our main HTML page

@app.route('/', methods=['GET'])
def home():
    return render_template('index_soph_form.html')


# This API returns song suggestions

@app.route('/bloodTest', methods=['GET'])
def suggest_song():
    age = float(request.args.get('age'))
    erythrocytes = float(request.args.get('erythrocytes'))
    haemoglobin = float(request.args.get('haemoglobin'))
    haematocrit = float(request.args.get('haematocrit'))
    leucocytes = float(request.args.get('leucocytes'))
    thrombocytes = float(request.args.get('thrombocytes'))
    mch = float(request.args.get('mch'))
    mchc = float(request.args.get('mchc'))
    mcv = float(request.args.get('mcv'))
    
    # extract all the necessary variables (inputs) by name
    # name of the individual inputs will be defined in JavaScript part of the HTML page, where the JS code is calling this server
    
    #if song == '':
    #    return ''


    myOrderedArrayOfInputs = [[haematocrit, haemoglobin, erythrocytes, leucocytes, thrombocytes, mch, mchc, mcv, age]]
    # build the "isputs array" - it may be also done in the prediction function itself, but anyways...
    
    
    # call the prediction function
    myResult = give_prediction(myOrderedArrayOfInputs)

    # render a html fragment with a visualized prediction result
    
    
    prediction = "Patient is recommended to stay in the hospital under supervision."
    if myResult == 0:
        prediction = "Patient can go home."
    
    return render_template('prediction.html', prediction_text=prediction)


if __name__ == '__main__':
    app.run()
