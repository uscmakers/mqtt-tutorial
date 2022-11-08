# import the necessary libraries
import paho.mqtt.client as mqtt
import time

# create an mqtt client
pub_client = mqtt.Client()

# connect it to the mqtt broker
pub_client.connect("test.mosquitto.org", 1883, 60)

# start
pub_client.loop_start()

# loop through this code
while (True):
	print("publishing...")
	# publish 1.23 to my topic
	pub_client.publish("MQTT_Simple/topic", 1.23)
	time.sleep(3)

