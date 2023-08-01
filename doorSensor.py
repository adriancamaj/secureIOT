# Secure IoT Door Sensor System
# doorSensor.py

# General Purpose Input/Output (GPIO)
# for Raspberry Pi
import RPi.GPIO as GPIO
# to make HTTP requests
import requests
# for sleep functionality
import time

# The GPIO pin that the door sensor is connected to:

DOOR_SENSOR_PIN = 14

# 'If This, Then That' (IFTTT) Web Applet Service
# Setup IFTTT Webhook URL to be triggered when door opens
# Replace 'your_ifttt_key' with actual IFTTT key

IFTTT_WEBHOOK_URL = "https://maker.ifttt.com/trigger/door_opened/with/key/your_ifttt_key"

# Broadcom SOC Channel (BCM)
# Set the pin numbering mode for the GPIO pins

GPIO.setmode(GPIO.BCM)

# Set pin as input and read data into the Raspberry Pi from the door sensor
# Uses a pull-up resistor to prevent floating state (unpredictable)
# circuit is open, door is closed => input pin will read as 'high' or binary 1
# circuit is closed, door is open => input pin will read as 'low' or binary 0

GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# forever loop
while True:
    # check the door sensor pin.
    if not GPIO.input(DOOR_SENSOR_PIN):
        # TRUE != 0 (Door is open)
        print("Door opened!") # print to console
        requests.post(IFTTT_WEBHOOK_URL) # trigger IFTTT POST request
    time.sleep(1) # Wait for a second before checking again (prevent CPU resource overload)
