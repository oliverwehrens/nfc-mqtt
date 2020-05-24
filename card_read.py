import nfc
import time
import paho.mqtt.client as mqtt

# got the idea from https://github.com/khan-farhan/Facility-management-using-NFC/blob/master/card_read.py

def after5s(started):

    return time.time() - started > 5


def read(client):

    clf = nfc.ContactlessFrontend('usb')

    def after5s(): return time.time() - started > 5
    started = time.time()

    tagx = clf.connect(rdwr={'on-connect': lambda tag: False}, terminate=after5s)
    tag = str(tagx)
    if tag != "":
       print(tag)
       tag = tag.split(" ")[-1]
       json = '{"uid":"'+tag[3:-1]+'", "response":"'+str(tagx)+'"}'
       client.publish("nfc/tag", json)
    


if __name__ == '__main__':

    client = mqtt.Client("nfcreader")
    client.connect("192.168.10.5", port=1883, keepalive=60, bind_address="") 
    while True:
       read(client)
