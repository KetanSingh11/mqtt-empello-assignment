# mqtt-empello-assignment
Assignment based on MQTT for Empello, London (https://www.empello.com)


### Question :
Create a simple "Hello World" MQTT PUB/SUB app.

- Subscriber should listen to the topic `/test`
- First publisher, with `/test/hello` sends *"hello"* every _1 second_ (feel free to use time.sleep(1))
- Second publisher, with the `/test/world` sends *"world"* every _2 second_.
- Please use this package: [paho-mqtt](https://pypi.org/project/paho-mqtt/) 

For a no-setup broker, feel free to use the one at [https://mosquitto.org](https://mosquitto.org)

Create a docker file with a working Django setup. What do you need to do to make it production-ready?


##### Project Dependencies

- linux os (with bash shell)
- Python 3.x
- virtualenv
- [test.mosquitto.org](test.mosquitto.org)


### Steps to run :

1. Clone the project
	
	`git clone https://github.com/KetanSingh11/mqtt-empello-assignment.git`

2. Open *2 tabs* in linux terminal, and navigate to the project directory.
3. In Tab #1 - run 

	`virtualenv venv`
	
	`source venv/bin/activate`

	`pip install -r requirements.txt`

3. In Tab #1 (_subscriber_) - run the command (the subscriber will start and wait for messages):
	
	`python subscriber.py`

4. In Tab #2 (_publisher_) - run the below command in order:
	
	`source venv/bin/activate`

	`chmod +x run.sh`
	
	`./run.sh`

5. Messages will start showing up in the Tab #1.

> By default the _publisher_ sends 5 messages and then shutsdown. To change this, update the value of `send_msg_count` in the `publisher.py` file to a integer number.