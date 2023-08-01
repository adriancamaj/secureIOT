# Secure IoT Door Sensor System

This repository contains the code for a simple, secure IoT door sensor system built with a Raspberry Pi. When the door sensor is triggered, it sends an alert via a secure HTTPS request (can be used to perform various actions, e.g. send SMS notification).

## Project Overview

The goal of this project is to demonstrate proficiency in both embedded systems and secure system design. The Raspberry Pi monitors the door sensor and sends an alert when the door is triggered. The alert is sent as a secure web request over HTTPS, showcasing the basic principles of secure communication in an IoT context.

## Requirements

- Python3
- Raspberry Pi with Raspbian installed and connected to the internet
- Door sensor connected to the Raspberry Pi's GPIO pin 14
- IFTTT account with a webhook configured

## Installation

You need to install the following Python packages:

- **RPi.GPIO** for accessing the GPIO pins on the Raspberry Pi.
- **requests** to make HTTP requests to IFTTT.

You can install these using pip:
```
pip install RPi.GPIO requests
```

## Configuration

In the **doorSensor.py** file:

Replace 'your_ifttt_key with your actual IFTTT key in the **IFTTT_WEBHOOK_URL** variable.

## Usage

To run the script, simply execute the Python file:

```
python3 doorSensor.py
```

The script will run in an infinite loop, checking the door sensor status every second. If the door is opened, it will print "Door opened!" to the console and send an HTTPS POST request to the IFTTT webhook.

## Disclaimer

The sensor operates in a normally closed state. If the sensor reads as 'high' or binary 1, the door is closed. If the sensor reads as 'low' or binary 0, the door is open. Make sure your door sensor is compatible with this configuration.

This project and its materials are provided for educational purposes only. While you're welcome to use this for your own projects, the author assumes no responsibility or liability for any misuse or operational security issues that may arise from its use.

## Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [MIT License](https://choosealicense.com/licenses/mit/) for details.
