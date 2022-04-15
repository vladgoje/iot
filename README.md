# Single project - Temperature and humidity sensor

The main idea of the project is to monitor the temperature in a room and send the data periodically to the pc where will be displayed on terminal.

Hardware requirements:
* Raspberry Pi Zero WH
* Micro SD card
* Raspberry Pi power supply
* DHT22 Temperature/Humidity Sensor
* Connectors

The DHT22 sensor has three pins that you will need to connect to your Pi Zero WH.

![1_Le68bdR4WoN9z0U-8px9cA](https://user-images.githubusercontent.com/62769184/163565621-52e113cd-9cb3-49fd-bd84-e0fd7999e3ad.jpeg)

* Sensor + sign will be connected to pin number 2.
* Sensor - sign will be connected to pin number 4.
* Sensor out symbol will be connected to pin number 7.

After configuring the raspberry pi for the first time, the following steps must be executed:

* sudo apt-get update
* sudo apt-get upgrade
* sudo pip3 install Adafruit_DHT


To run the script:
python3 tempsensor.py
