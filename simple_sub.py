# import the necessary libraries
import paho.mqtt.client as mqtt
import time

# when we connect to the mqtt broker, subscribe to my topic
def connect_fn(client, userdata, flags, rc):
    client.subscribe("MQTT_Simple/topic")
    # specify what to do when messages are received on this topic
    client.message_callback_add("MQTT_Simple/topic", callback_fn1)

# when we receive messages, print them
def callback_fn1(client, userdata, message):
	print("Received a message on:", message.topic, "therefore running callback_fn1")
	print("Received the message:", message.payload)
	# do whatever else here...

# create an mqtt client
sub_client = mqtt.Client()

# specify what to do when we connect
sub_client.on_connect = connect_fn

# connect to the mqtt broker
sub_client.connect("test.mosquitto.org", 1883, 60)

# start
sub_client.loop_start()

while (True):
    time.sleep(1)
    # do whatever

