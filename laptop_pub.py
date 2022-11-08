"""EE 250L Lab 04 Starter Code (edited by Caleb)

Run vm_publisher.py in a separate terminal on your laptop."""

import paho.mqtt.client as mqtt
import time
#from pynput import keyboard

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k == 'o':
        print("o")
        # send "LED_ON"
        client.publish("MQTT_Adv/led", "LED_ON")
    elif k == 'f':
        print("f")
        # send "LED_OFF"
        client.publish("MQTT_Adv/led", "LED_OFF")
        

if __name__ == '__main__':
    #setup the keyboard event listener
    # lis = keyboard.Listener(on_press=on_press)
    # lis.start() # start to listen on a separate thread

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    #client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()


    while True:
        with lock:
            x = input("Type 'o' to turn LED on & type 'f' to turn LED off")
            if x == 'o':
                print("o")
                # send "LED_ON"
                client.publish("MQTT_Adv/led", "LED_ON")
            elif x == 'f':
                print("f")
                # send "LED_OFF"
                client.publish("MQTT_Adv/led", "LED_OFF")
        time.sleep(1)

