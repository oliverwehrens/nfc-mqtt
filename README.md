# Simple NFC to MQTT Service

This connects a NFC Reader (like ACR122U-A9) to MQTT. It will publish the UID to the MQTT Server.

This is a result of a rainy sunday afternoon hack. 

## Requirements

You need to have libnfc installed on your system.

I followed https://oneguyoneblog.com/2015/09/16/acr122u-nfc-usb-reader-raspberry-pi/

Furthermore it requires the python-libs mentioned in requirements.txt.

```shell script
pip install -r requirements.txt
```
## Things which you want to configure:

- MQTT Server in nfc2mqtt_service.py

Yes, this could go into a configuration file.

## Install & Run

After configuration run ./install.sh to copy the systemd file in it's place and enable and start the service.
The nfc2mqtt_service.py will be copied to /usr/local/bin.

## FAQ

*Is this work in progress?*

Yes, it is.

*Does it work?*

It works for me ;-). PRs are welcome.

*How do I remove it?*

```shell script
sudo systemctl stop nfc2mqtt.service
sudo systemctl disable nfc2mqtt.service
sudo rm /etc/systemd/system/nfc2mqtt.service
rm /usr/local/bin/nfc2mqtt_service.py
```
