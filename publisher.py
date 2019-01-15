###!/usr/bin/env python3
import paho.mqtt.client as mqtt
from datetime import datetime
import time


HOST="localhost"
PORT=1883
KEEP_ALIVE=60

send_msg_count = 5


client = mqtt.Client()
client.connect(HOST, PORT, KEEP_ALIVE)

print("Publishing {} messages in intervals of 2 sec...".format(send_msg_count))

while send_msg_count > 0:
	print(".")
	client.publish("topic/test", "Hello world! @ {}".format(datetime.now()));
	time.sleep(2)
	send_msg_count -= 1


#send pkill
client.publish("topic/test", "KILLME");

client.disconnect()
print("DONE.\nDisconnected!")

