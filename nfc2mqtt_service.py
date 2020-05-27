import time

import nfc
import paho.mqtt.client as mqtt

# see https://readthedocs.org/projects/nfcpy/downloads/pdf/develop/ for more options


class TagScan:
    def __init__(self, client_mqtt):
        self.last_known_tag_id = None
        self.tag_connect_time = 0
        self.client = client_mqtt
        self.terminate = False

    def scan(self):
        print("Scan Starting ..")
        self.terminate = False
        clf = nfc.ContactlessFrontend("usb")
        print("CLF established.")
        rdwr_options = {
            "on-connect": self.on_tag_connect,
            "on-release": self.on_tag_release,
            "beep-on-connect": False,
        }
        while not self.terminate:
            print("CLF connecting.")
            clf.connect(rdwr=rdwr_options, terminate=lambda: self.terminate)
        print("CLF close.")
        clf.close()

    def on_tag_connect(self, tag):
        print("Tag connect: " + str(tag))
        now = time.time()
        tag_id = str(tag).split(" ")[-1][3:-1]
        if self.last_known_tag_id != tag_id or now > self.tag_connect_time + 1:
            print("Send MQTT message.")
            json = '{"uid":"' + tag_id + '", "response":"' + str(tag) + '"}'
            mqtt_client.connect("192.168.10.5", port=1883, keepalive=60, bind_address="")
            self.client.publish("nfc/tag", json)
            mqtt_client.disconnect()
            self.last_known_tag_id = tag_id
            self.tag_connect_time = time.time()
            self.terminate = True
        return True

    def on_tag_release(self, tag):
        print("Tag release: " + str(tag))
        return True


if __name__ == "__main__":
    mqtt_client = mqtt.Client("nfcreader")
    scanner = TagScan(mqtt_client)
    while True:
        scanner.scan()
