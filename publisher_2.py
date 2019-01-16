# import multiprocessing
# import time

# def test(name):
#     # f = '{}.txt'.format(name)
#     file = open("fff.txt", "w")
#     file.write(msg) 
#     file.close()    



# if __name__ == "__main__":
#     print("Initializing 2 worker publishers")
    
#     pool = multiprocessing.Pool(3)

#     x=pool.apply_async(test, args=("d1"))
#     y=pool.apply_async(test, args=("d2"))
#     pool.close()
#     pool.join()

#     time.sleep(10)
#     print("done")


import paho.mqtt.client as mqtt
from datetime import datetime
import time
from publisher import create_connection, BROKER_HOST


def publisher_start(client, topic, msg, interval_sec=1):
    """
    Publishes messages to broker
    """
    global BROKER_HOST
    print("Publishing 5 messages to broker `{}` in intervals of {} sec...".format(BROKER_HOST, interval_sec))
    send_msg_count = 5

    while send_msg_count > 0:
        try:        
            print(".")
            client.publish(topic, "{} @ {}".format(msg, datetime.now()));
            time.sleep(interval_sec)
            send_msg_count -= 1
        except KeyboardInterrupt:
            print("Terminating..")
            return

    #send pkill
    client.publish(topic, "KILLME");



if __name__ == "__main__":
    client = create_connection()
    publisher_start(client, "test/world", "world", 2)

    client.disconnect()

