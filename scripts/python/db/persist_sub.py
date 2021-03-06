
import json
import paho.mqtt.client as mqtt
import urlparse
import sys

    
from tinydb import TinyDB, Query
db = TinyDB('db.json')

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_message(client, obj, msg):

    print("Inserting into DB:"+msg.payload)
   
    msg_json=json.loads(msg.payload)
    db.insert(msg_json)
  
    db.insert(msg.payload)


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed,  QOS granted: "+ str(granted_qos))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# parse mqtt url for connection details
url_str = 'mqtt://iot.eclipse.org:1883/jimtheenchanter/home'
url = urlparse.urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe(base_topic +"/temperature", 0)
mqttc.subscribe(base_topic +"/humidity", 0)
mqttc.subscribe(base_topic +"/pressure", 0)


mqttc.loop_forever()

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))


