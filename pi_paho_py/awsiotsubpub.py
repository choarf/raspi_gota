#!/usr/bin/python

# this source is part of my Hackster.io project:  https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will subscribe and show all the messages sent by its companion
# awsiotpub.py using the AWS IoT hub

import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
import datetime


SYS_msg ="""{
  "cpu_load": 1.01,
  "cpu_Temp": 11,
  "temperature": 10,
  "pH_agua": 8.77,
  "turbidez": 60,
  "timestamps": 1676069113012
}"""

Json_msg_init = """{
    """
Json_msg_end = """
    "cpu_load": 1.01,
    "cpu_Temp": 11,
    "temperature": 10,
    "pH_agua": 8.77,
    "turbidez": 60,
    "timestamps": 1676069113012
}"""



def timestamp():
    ct = datetime.datetime.now()
    rastime = '"raspitstamp" : ' + str(ct.timestamp())
    return rastime

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))

#def on_log(client, userdata, level, msg):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log
awshost = "a2zzu55sjawy4x-ats.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "gota_sense"
thingName = "gota_sense"

caPath = "./certs/AmazonRootCA1.pem"
certPath = "./certs/certificate.pem.crt"
keyPath = "./certs/private.pem.key"



mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)
while 1==1:
    sleep(5)
    msg =Json_msg_init + timestamp()+',' + Json_msg_end

    mqttc.publish("GOTA/gota_test", msg, qos=1)

#mqttc.loop_forever()
    mqttc.loop_start()
