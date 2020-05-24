# Simple NFC to MQTT Service

This connects a NFC Reader (like ACR122U-A9) to MQTT. It will publish the UID to the MQTT Server.

This is a result of a rainy sunday afternoon hack. 

## Requirements

You need to have libnfc installed on your system. I used a Raspberry Pi with Raspbian Minimal.

I followed https://oneguyoneblog.com/2015/09/16/acr122u-nfc-usb-reader-raspberry-pi/

```shell script
sudo apt-get update -y
sudo apt-get -y install subversion autoconf debhelper flex libusb-dev libpcsclite-dev libpcsclite1 libccid pcscd pcsc-tools libpcsc-perl libusb-1.0-0-dev libtool libssl-dev cmake checkinstall
sudo apt-get -y install python3 pip3
git clone https://github.com/nfc-tools/libnfc.git
cd nfclib
autoreconf -vis
./configure -prefix=/usr -sysconfdir=/etc --with-drivers=acr122_usb
make
sudo make install
vi  /etc/modprobe.d/blacklist.conf
```
added to that file:
```shell script
blacklist pn533
blacklist nfc
```

Next:

```shell script
sudo udevadm control -R
reboot
```

Furthermore it requires the python-libs mentioned in requirements.txt.

```shell script
pip install -r requirements.txt
```
## Things which you want to configure:

- MQTT Server in nfc2mqtt_service.py
- You can also edit the MQTT topic 

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
