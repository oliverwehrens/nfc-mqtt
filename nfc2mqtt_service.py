import json
import time

import nfc
import paho.mqtt.client as mqtt

# see https://readthedocs.org/projects/nfcpy/downloads/pdf/develop/ for more options


def find_tag_type(tag_info: str) -> str:
    return tag_info.split(" ")[0]


def get_id(tag_info: str) -> str:
    split = tag_info.split(" ")[-1]
    return split[3 : len(split)]


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

    def tag_is_not_last_scanned_tag(self, tag_id):
        return self.last_known_tag_id != tag_id

    def scan_timeout_has_passed(self) -> bool:
        now = time.time()
        return now > self.tag_connect_time + 1

    def on_tag_connect(self, tag):
        print("Tag connect: " + str(tag))
        tag_id = get_id(str(tag))
        if self.tag_is_not_last_scanned_tag(tag_id) or self.scan_timeout_has_passed():
            data = {"uid": tag_id, "tag_type": find_tag_type(str(tag)), "response": str(tag)}
            self.publish_to_mqtt(data)
            self.last_known_tag_id = tag_id
            self.tag_connect_time = time.time()
            self.terminate = True
        return True

    def publish_to_mqtt(self, data):
        mqtt_client.connect("192.168.10.5", port=1883, keepalive=60, bind_address="")
        print("Send MQTT message.")
        self.client.publish("nfc/tag", json.dumps(data))
        mqtt_client.disconnect()

    def on_tag_release(self, tag):
        print("Tag release: " + str(tag))
        return True


if __name__ == "__main__":
    mqtt_client = mqtt.Client("nfcreader")
    scanner = TagScan(mqtt_client)
    while True:
        scanner.scan()
