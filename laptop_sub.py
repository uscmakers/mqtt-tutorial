"""EE 250L Lab 04 Starter Code (edited by Caleb)

Run vm_subscriber.py in a separate terminal on your laptop."""

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("MQTT_Adv/button") # subscribe to button channel
    client.message_callback_add("MQTT_Adv/button", buttonCallback) # add custom call back function for button messages

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

# custom callback for button
def buttonCallback(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload, "utf-8"))
    
if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()

    while True:
        time.sleep(1)
