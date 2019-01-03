# iot-greenhouse-app

James OBrien
20082197
Computer Science & Networking Assignment
January 2019

Dashboard url:
http://assignment1.jimwithaj.com/thingspeak.html

Youtube Video:
https://youtu.be/NOwSJjczkzg

SUMMARY
Sensor-driven system allowing users to monitor and control indoor 

growing conditions
. User gets Twitter updates if light falls below a 

certain amount of lumins.

Data is stored in a database on designated Pi and on cloud aggregator, 

Thingspeak.com

HOW IT WORKS
Server:
Raspberry Pi with SenseHat is publishing humidity, temperature and 
pressure through MQTT and to Thingspeak using Python.
It also has a javascript file on it with node.js framework installed to 
allow a remote device, such as a smartphone, to turn on and off a light.
ThingSpeak has a react set up to send a Tweet to the users' Twitter page 
if the light lumins fall below 80. In which case the user can decide to 
turn on the light.

client_pub_mult.py
index.js

Database:
A second Raspberry Pi is subscribing using paho.mqtt.client and 
exporting to a db.json using TinyDB.
This database Pi also has useful scripts which contain functions which 
can be used to mainulate the gathered data eg. average temp over a 
certain time period.

sense_api.py 
temp_db_data.py
db.json


HARDWARE:
2 x Raspberry Pi's
Sensehat
2 x smart phones
PC/Laptop/Tablet 

Languages Used:
Python
JavaScript
HTML/CSS
Java

Also used:
Blynk Software, Node.js platform

