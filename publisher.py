import multiprocessing
import threading
import sys

import paho.mqtt.client as mqtt
from datetime import datetime
import time
import signal


BROKER_HOST="localhost"
# BROKER_HOST="test.mosquitto.org"
PORT=1883
KEEP_ALIVE=60
TOPIC_LIST=["test/world", "test/hello",]

send_msg_count = 5

# def init_worker():
#     signal.signal(signal.SIGINT, signal.SIG_IGN)

def create_connection():
    """
    Establishes a connection to a broker
    """
    client = mqtt.Client()
    client.connect(BROKER_HOST, PORT, KEEP_ALIVE)
    return client

def disconnect_connection(topics):
    """
    Disconnects from the broker, sends kill signal to subscribers
    """
    #send pkill
    for topic in topics:
        client.publish(topic, "KILLME");

    client.disconnect()
    print("DONE.\nDisconnected!")


def publisher_start(client, topic, msg, interval_sec=1, queue=None):
    """
    Publishes messages to broker
    """
    broker_host = queue.get()
    print("yes")
    with open('{}.txt'.format(msg), "w+") as file:
        file.write(msg)
        file.close()

    queue.put(broker_host)

    print("Publishing messages to broker `{}` in intervals of {} sec...".format(broker_host, interval_sec))

    while send_msg_count > 0:
        try:        
            print(".")
            client.publish(topic, "{} @ {}".format(msg, datetime.now()));
            time.sleep(interval_sec)
            send_msg_count -= 1
        except KeyboardInterrupt:
            print("Terminating..")
            return

def test(name):
    for i in range(5):
        print("{} : xxx".format(name))
        time.sleep(2)
        sys.stdout.flush()
        
    file = open('{}.txt'.format(name), "w")
    file.write(msg) 
    file.close()    



if __name__ == "__main__":
    client = create_connection()
    print("Initializing 2 worker publishers")
    
    queue = multiprocessing.Queue()
    queue.put(BROKER_HOST)

    pool = multiprocessing.Pool(3)

    try:
        # pool.apply_async(publisher_start, args=(client, "test/hello", "hello", 1, queue))
        # pool.apply_async(publisher_start, args=(client, "test/world", "world", 2, queue))
        
        pool.apply_async(test, args=("d1"))
        pool.apply_async(test, args=("d2"))

        print()
        time.sleep(10)
        # pool.close()
        # pool.join()

    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
        pool.join()
        disconnect_connection(TOPIC_LIST)

    disconnect_connection(TOPIC_LIST)

    # else:
    #     pool.close()
    #     pool.join()
    #     disconnect_connection()

    # disconnect_connection()

    # threads = []

    # try:
    #     t1 = threading.Thread(target=publisher_start, args=(client, "test/hello", 1))
    #     t1.start()
    #     t1.join()
    #     threads.append(t1)
    #     t2 = threading.Thread(target=publisher_start, args=(client, "test/world", 2))
    #     t2.start()
    #     t2.join()
    #     threads.append(t2)

    # except KeyboardInterrupt:
    #     print("Received keyboard interrupt, quitting threads.")
    #     for t in threads:
    #         if t.is_alive():


    print("done")
