import paho.mqtt.client as mqtt

# This is the Subscriber

BROKER_HOST="localhost"
# BROKER_HOST="test.mosquitto.org"
PORT=1883
KEEP_ALIVE=60

def on_connect(client, userdata, flags, rc):
	print("Connecting to broker '{}' ...".format(BROKER_HOST), end="")
	if rc==0:
		client.subscribe("test/#")
		print("DONE")
		print("Connected OK with result code = " + str(rc))
		print(">Now waiting for messages...\n\n")
	else:
		print("FAILED")
		print(">Bad connection Returned code = ", str(rc))

def on_message(client, userdata, msg):
	payload_msg = msg.payload.decode()
	
	if payload_msg.upper() == "KILLME":
		print(">Shutdown signal received. SHUTTING DOWN Subscriber!!")
		client.disconnect()

	print(msg.topic + " " + str(payload_msg))
	


client = mqtt.Client()
client.connect(BROKER_HOST, PORT, KEEP_ALIVE)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

