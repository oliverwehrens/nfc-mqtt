sudo cp nfc2mqtt.service /etc/systemd/system/nfc2mqtt.service
sudo cp nfc2mqtt_service.py /usr/local/bin/nfc2mqtt_service.py
sudo systemctl enable nfc2mqtt.service
sudo systemctl start nfc2mqtt.service
