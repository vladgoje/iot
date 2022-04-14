import Adafruit_DHT # library for dht sensor
import time

DHT_SENSOR = Adafruit_DHT.DHT22 # dht temperature sensor type
DHT_PIN = 4 # GPIO Pin number

while True:
	# Read the temperature and humidity from sensor
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	
	# If humidity and temperature is detected, print them on terminal
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
	else:
		print("Sensor failure. Check wiring.")
	time.sleep(3);