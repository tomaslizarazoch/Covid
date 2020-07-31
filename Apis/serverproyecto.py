import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
from data import covid
import requests
import numpy as np



    



# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    # Redirect

    return '<h1> Api Grupo A <h1> <body text = "green" bgcolor="black" <p>Para obtener tu token usa enpoint: /get_token?id= _._._._ <p> <p1>Si tardamos mucho es que estamos lejos de vacaciones y es mejor que trabajes con otra data. <p1>  <p2> Adios y Feliz Verano <p2>'


@app.route("/give_me_id", methods =['GET'])
def give_id(): 
    x= request.args['id']
    return x

@app.route("/get_token", methods = ['GET'])
def get_token():
    clave = None
    token = {'token':'YA3168907Y3523932R70885197wy3148051D'}
    if 'id' in request.args: 
        clave = str(request.args['id'])
    if clave == 'A137':
        return token 
    else:
        return "try another time"

@app.route("/get_data", methods = ['GET'])
def get_json():
    eltoken = None
    eljson = covid('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    if 'id' in request.args:
        eltoken = str(request.args['id'])
    if eltoken == 'YA3168907Y3523932R70885197wy3148051D':
        return eljson.to_json()

   

def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "/set.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()
