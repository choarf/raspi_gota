#!/usr/bin/python3

# this source is part of my Hackster.io project:  https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will publish test mqtt messages using the AWS IoT hub
# to test this program you have to run first its companion awsiotsub.py
# that will subscribe and show all the messages sent by this program

import paho.mqtt.client as paho
import os
#import socket
import ssl
from time import sleep
from random import uniform


SYS_msg ="""{
  "cpu_load": 1.01,
  "cpu_Temp": 11,
  "temperature": 10,
  "pH_agua": 8.77,
  "turbidez": 60,
  "timestamps": 1676069113012
}"""

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
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

#**************Init mqtt -----------------

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

# *************** loop *****************


while 1==1:
    sleep(0.5)
    if connflag == True:


        mqttc.publish("GOTA/gota_s1_SYS", SYS_msg, qos=1)
        print("msg sent:  " + SYS_msg )
        #mqttc.publish("temperature", tempreading, qos=1)
        #print("msg sent: temperature " + "%.2f" % tempreading )
    else:
        print("waiting for connection...")
