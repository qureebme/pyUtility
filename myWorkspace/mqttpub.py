import paho.mqtt.client as mqtt
import time
publisher = mqtt.Client('Publisher')

def on_connect(client, userdata, flags, rc):
    print("Publisher connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+ str(msg.payload))

publisher.connect("localhost", 5000, 60)

publisher.on_message = on_message
publisher.on_connect = on_connect

#publisher.loop_forever()
while(True):
    res = publisher.publish('data/value', 58796)
    print(res.rc)
    print(res.is_published)
    print("\n")
    time.sleep(5)
