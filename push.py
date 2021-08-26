# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

def pushmessageHNV(msg):
    client = mqtt.Client('pymooncake')
    client.username_pw_set("jjy000", "qazwsxedc123")
    client.connect('mqtt.arduino-hannover.de', port=1883)
    client.publish('jjy000/mooncake', msg)

# client.connect('test.mosquitto.org', port=1883)
