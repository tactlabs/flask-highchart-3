'''
Source:

Author: Raja CSP


'''
from flask import Flask, render_template, jsonify
import random
import json

app  = Flask(__name__)
PORT = 3017

FILEPATH = "data.json"
    
'''
    http://0.0.0.0:3017/

    https://www.youtube.com/watch?v=wgfc07NJskY
'''
@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    return render_template("index.html")

'''
    http://0.0.0.0:3017/data

'''
@app.route("/data", methods=["GET"])
def read_json():

    district_list = ['Chennai', 'Coimbatore', 'Trichy', 'Salem', 'Kanyakumari', 'Pondicherry']

    college_list = [90, 71, 87, 30, 25, 86]

    result_dict = {
        'district'      : district_list,
        'title'         : 'No.Of.College in Districts',
        'college_data'  : college_list 
    }

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run( debug = True, host="0.0.0.0", port = PORT)
    