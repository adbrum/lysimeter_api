#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from pymongo import MongoClient
# importing the requests library 
import requests 


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("LISIMETRO")

def on_message(client, userdata, msg):
    
    receiveTime=datetime.now()
    message=json.loads(msg.payload.decode("utf-8"))

    data = {
                "lysimeter": message['ID'],
                "battery": message['SVB'],
                "ambient_temperature": message['STA'],
                "ambient_humidity": message['SHA'],
                "ambient_light01": message['SL_1'],
                "ambient_light02": message['SL_2'],
                "soil_temperature01": message['STS1'],
                "soil_temperature02": message['STS2'],
                "soil_temperature03": message['STS3'],
                "soil_humidity01": message['SHS1'],
                "soil_humidity02": message['SHS2'],
                "soil_humidity03": message['SHS3'],
                "sediment_weight": message['SPR'],
                "lysimeter_weight": message['SPL']
            }

    # api-endpoint 
    URL = "http://ietsis.dynu.net:9000/api/token/"
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {
                "username": "admin",
                "password": "admin"
             }
    
    # sending get request and saving the response as response object 
    res = requests.post(url = URL, data = PARAMS) 
    
    # extracting data in json format 
    token = res.json() 

    print('TOKEN:' , token['access'])
    
    # defining the api-endpoint  
    API_ENDPOINT = "http://ietsis.dynu.net:9000/lysimeters/"

    # sending post request and saving response as response object 
    res = requests.post(url = API_ENDPOINT, headers={ 'Authorization': 'Bearer ' +  token['access']}, data = data) 
    
    # extracting response text  
    saved = res.text 
    print("The Lysimeter data is:%s"%saved) 

    #collection.insert_one(data)


# Set up client for MongoDB
#mongoClient=MongoClient()
#db=mongoClient.lysimeter
#collection=db.lysimeter_deviceparams

# Initialize the client that should connect to the Mosquitto broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.105", 1883, 60)

# Blocking loop to the Mosquitto broker
client.loop_forever()