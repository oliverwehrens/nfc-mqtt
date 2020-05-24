# Simple NFC to MQTT Service

This connects a NFC Reader (like ACR122U-A9) to MQTT. It will publish the UID to the MQTT Server.
This code is a result of a 2h hack (which was mostly installing libs and trying to find out how NFC works). 


You need to have libnfc installed on your system.
Furthermore it requires the python-libs mentioned in requirements.txt.


## Things which you want to configure:

- MQTT Server in nfc_service.py
- Location of the service.py in nfc.service

## Install & Run

After configuration run ./install.sh to copy the systemd file in it's place and enable and start the service.


## FAQ

*Is this work in progess?*

Yes, it is.
