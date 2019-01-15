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

