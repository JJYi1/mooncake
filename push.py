# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
username = 'your user name'
pwd = 'your password'
server = 'your server'
channel = 'your channel'

def pushmessageHNV(msg):
    client = mqtt.Client('pymooncake')
    client.username_pw_set(username, pwd)
    client.connect(server, port=1883)
    client.publish(channel, msg)

# client.connect('test.mosquitto.org', port=1883)
