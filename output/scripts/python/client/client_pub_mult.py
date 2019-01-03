import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import urlparse
import urllib2
import sys
import time
import json
#from wia import Wia

from sense_hat import SenseHat


TEMP_API_KEY='OF54OOUP7AN4GKQO'
tempbaseURL='https://api.thingspeak.com/update?api_key=%s' % TEMP_API_KEY
HUMIDITY_API_KEY='TQU0QN6215BQJGDK'
humiditybaseURL='https://api.thingspeak.com/update?api_key=%s' % HUMIDITY_API_KEY
PRESSURE_API_KEY='RS3HUDO0J1PL5U73'
pressurebaseURL='https://api.thingspeak.com/update?api_key=%s' % PRESSURE_API_KEY

sense = SenseHat()
sense.clear()

#wia = Wia()
#wia.access_token = "d_sk_5Jt3CGbhvWpKS7bLj2Br0qyk"

# parse mqtt url for connection details
url_str = 'mqtt://iot.eclipse.org:1883/jimtheenchanter/home'
print(url_str)
url = urlparse.urlparse(url_str)
base_topic = url.path[1:]
auth=None
# Connect
if (url.username):
    auth = {'username':url.username, 'password':url.password}

def writeData(temp, humidity, pressure):
	#sending the data to thinkspeak in the query string
	conn1 = urllib2.urlopen(tempbaseURL + '&field1=%s' % (temp))
	conn2 = urllib2.urlopen(humiditybaseURL + '&field1=%s' % (humidity))
	conn3 = urllib2.urlopen(pressurebaseURL + '&field1=%s' % (pressure))
	print(conn1.read())
	print(conn2.read())
	print(conn3.read())
	#closing the connection
	conn1.close()
	conn2.close()
	conn3.close()


#def writeData(humidity):
#	#sending the data to thinkspeak in the query string
#	conn2 = urllib2.urlopen(humiditybaseURL + '&field1=%s' % (humidity))
#	print(conn2.read())
#	#closing the connection
#	conn2.close()

#def writeData(pressure):
#	#sending the data to thinkspeak in the query string
#	conn3 = urllib2.urlopen(pressurebaseURL + '&field1=%s' % (pressure))
#	print(conn3.read())
#	#closing the connection
#	conn3.close()

# Publish a message
while True:
    temp=round(sense.get_temperature(),2)
#   wia.Event.publish(name="temperature", data=temp)
#   writeData(temp, humidity, pressure)
    sense.show_message(str(temp))
    
    humidity=round(sense.get_humidity(),2)
#   wia.Event.publish(name="humidity", data=humidity)
#   writeData(humidity)
    sense.show_message(str(humidity))
       
    pressure=round(sense.get_pressure(),2)
#   wia.Event.publish(name="pressure", data=pressure)
#   writeData(pressure)
    sense.show_message(str(pressure))

    writeData(temp, humidity, pressure)
    #Create JSON strings
    temp_sensor=json.dumps({"temperature":temp, "timestamp":time.time()}) 
    humidity_sensor=json.dumps({"humidity":humidity, "timestamp":time.time()}) 
    pressure_sensor=json.dumps({"pressure":pressure, "timestamp":time.time()})

    #Create array of MQTT messages
    temp_msg={'topic': base_topic +"/temperature", 'payload':temp_sensor}
    hum_msg={'topic': base_topic +"/humidity", 'payload':humidity_sensor}
    press_msg={'topic' : base_topic +"/pressure", 'payload':pressure_sensor }
    
    msgs=[temp_msg,hum_msg, press_msg]

    #Publish array of messages
    publish.multiple(msgs, hostname=url.hostname, port=url.port, auth=auth)
    print("published")
    time.sleep(180)
