# gota_raspi
Gota project on raspi

Set up raspi
sudo apt-get update / upgrade
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install python3-numpy
sudo apt-get install python3-pandas

sudo pip3 install paho-mqtt
sudo pip3 install pytz
sudo pip3 install socket

# configure with MQTT & AWS
init.py 

# mqtt
SysTopic = "GOTA/sandbox/Sys"
SensTopic = "GOTA/sandbox/Sens"

# aws
awshost = "a2zzu55sjawy4x-ats.iot.us-east-1.amazonaws.com"
awsport = 8883

caPath = "./certs/AmazonRootCA1.pem"
certPath = "./certs/certificate.pem.crt"
keyPath = "./certs/private.pem.key"

