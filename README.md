# Simple NFC to MQQT Service

This connects a NFC Reader (like ACR122U-A9) to MQTT. It will publish the UID to the MQTT Server.

You need to have libnfc installed on your system.
Furthermore it requires the python-libs mentioned in requirements.txt.


Things which you want to configure:

- MQTT Server in card_read.py
- Location of the card_read.py in nfc.service


