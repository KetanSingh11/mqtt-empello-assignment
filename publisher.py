###!/usr/bin/env python3
import paho.mqtt.client as mqtt
from datetime import datetime
import time
import sys

# BROKER_HOST="localhost"
BROKER_HOST="test.mosquitto.org"
PORT=1883
KEEP_ALIVE=60
send_msg_count = 5


def create_connection():
    """
    Establishes a connection to a broker
    """
    client = mqtt.Client()
    client.connect(BROKER_HOST, PORT, KEEP_ALIVE)
    return client

def publisher_start(client, topic, msg, interval_sec=1, kill=False):
    """
    Publishes messages to broker
    """
    global BROKER_HOST, send_msg_count
    print("Publishing {} messages to broker `{}` in intervals of {} sec...".format(send_msg_count, BROKER_HOST, interval_sec))
    
    while send_msg_count > 0:
        try:        
            print(".")
            # client.publish(topic, "{} @ {}".format(msg, datetime.now()));
            client.publish(topic, "{}".format(msg));
            time.sleep(interval_sec)
            send_msg_count -= 1
        except KeyboardInterrupt:
            print("Terminating..")
            return

    #send pkill
    if kill:
        client.publish(topic, "KILLME");



if __name__ == "__main__":
    print(len(sys.argv))

    if len(sys.argv) < 2:
        print("Parameters missing. Exited")
        sys.exit(1)

    topic = sys.argv[1]
    msg = sys.argv[2]
    time_gap = int(sys.argv[3])
    
    try:
        kill_subscriber = sys.argv[4]
    except Exception:
        kill_subscriber = False


    client = create_connection()
    publisher_start(client, topic, msg, time_gap, kill_subscriber)

    client.disconnect()
    print("DONE.\nDisconnected!")

