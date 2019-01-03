import time
from wia import Wia
from sense_hat import SenseHat
sense = SenseHat()

wia = Wia()
wia.access_token = "d_sk_5Jt3CGbhvWpKS7bLj2Br0qyk"

temp=round(sense.get_temperature(),2)
wia.Event.publish(name="temperature", data=temp)

humidity=sense.get_humidity()
wia.Event.publish(name="humidity", data=humidity)

pressure=sense.get_pressure()
wia.Event.publish(name="pressure", data=pressure)

time.sleep(15)
