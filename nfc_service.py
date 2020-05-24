import nfc
import paho.mqtt.client as mqtt

# see https://readthedocs.org/projects/nfcpy/downloads/pdf/develop/ for more options


class TagScan:
    def __init__(self, client_mqtt):
        self.last_known_tag_id = None
        self.client = client_mqtt
        self.terminate = False

    def run(self):
        clf = nfc.ContactlessFrontend("usb")
        rdwr_options = {
            "on-connect": self.on_tag_connect,
            "on-release": self.on_tag_release,
            "beep-on-connect": False,
        }
        while not self.terminate:
            clf.connect(rdwr=rdwr_options, terminate=lambda: self.terminate)

    def on_tag_connect(self, tag):
        tag_id = str(tag).split(" ")[-1][3:-1]
        if self.last_known_tag_id != tag_id:
            json = '{"uid":"' + tag_id + '", "response":"' + str(tag) + '"}'
            self.client.publish("nfc/tag", json)
            self.last_known_tag_id = tag_id
        return True

    def on_tag_release(self, tag):
        return True


if __name__ == "__main__":
    client = mqtt.Client("nfcreader")
    client.connect("192.168.10.5", port=1883, keepalive=60, bind_address="")
    scanner = TagScan(client)
    scanner.run()
