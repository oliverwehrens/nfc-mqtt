import nfc
import time
import paho.mqtt.client as mqtt
import datetime

# got the idea from https://github.com/khan-farhan/Facility-management-using-NFC/blob/master/card_read.py

def after5s(started):

    return time.time() - started > 5


def read(client):

    last_known_tag = "None"
    clf = nfc.ContactlessFrontend('usb')
    while True:
       def after5s(): return time.time() - started > 5
       started = time.time()

       tag = clf.connect(rdwr={'on-connect': lambda tag: False}, terminate=after5s)
       clf.close()
       tag = str(tag)
       tag_id = tag.split(" ")[-1][3:-1]
       if tag_id != last_known_tag:
          print(tag)
          json = '{"uid":"'+tag_id+'", "response":"'+str(tag)+'"}'
          client.publish("nfc/tag", json)
          last_known_tag = tag_id



if __name__ == '__main__':

    client = mqtt.Client("nfcreader")
    client.connect("192.168.10.5", port=1883, keepalive=60, bind_address="")
    read(client)
