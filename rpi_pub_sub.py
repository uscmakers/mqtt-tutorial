"""EE 250L Lab 04 Starter Code (edited by  Caleb)

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import sys
import threading

from gpiozero import LED
from gpiozero import Button

lock = threading.Lock()


# Defining ports for LED and Button
led = LED(4)
button = Button(17)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("MQTT_Adv/led") #subscribe to LED channel
    client.message_callback_add("MQTT_Adv/led", ledCallback)

def ledCallback(client, userdata, msg):
    new_msg = str(msg.payload, "utf-8")
    # new_msg = msg.decode('utf8', 'strict')
    with lock:
        if(new_msg == "LED_ON"):
            print("Turning the LED on")
            led.on()
        elif(new_msg == "LED_OFF"):
            print("Turning LED off")
            led.off()

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    #client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()

    while True:
        with lock:
            if(button.is_pressed):
                client.publish("MQTT_Adv/button", "Button pressed!")
        time.sleep(1)
