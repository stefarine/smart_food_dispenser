# Project Overview and Folder Structure

This document provides a summary of the Smart Food Dispenser project and explains the organization of the files and folders in the repository.

## Components

### Hardware
- 2x [M5Stack Core2](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)*
- [Laser.tx unit](https://shop.m5stack.com/products/laser-tx-unit)
- [Laser.rx unit](https://shop.m5stack.com/products/laser-rx-unit)
- [Servo kit 360°](https://shop.m5stack.com/products/servo-kit-360)
- [Motion sensor](https://shop.m5stack.com/products/pir-module)
- A computer and its webcam**
- A 3D printer or some DIY skills

### Software
- [Google Cloud Functions](https://cloud.google.com/functions)
- [Google Cloud Storage](https://cloud.google.com/storage)
- [Google Vision API](https://cloud.google.com/vision)
- [Adafruit IO MQTT feeds](https://io.adafruit.com/)
- [Flask server](https://flask.palletsprojects.com/)
- [Streamlit web application](https://streamlit.io/)
- [Twilio](https://www.twilio.com/)

## Code

The code for the Smart Food Dispenser is divided into several scripts that handle different aspects of the system:

- [`feeding-csv.py`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/Cloud/feeding-csv.py): This Python script is a Google Cloud Function that writes the current date and time to a CSV file in a Google Cloud Storage bucket whenever the dog is fed. 

- [`laser-csv.py`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/Cloud/laser-csv.py): This Python script is a Google Cloud Function that writes the current date and time to a CSV file in a Google Cloud Storage bucket whenever the food tank is empty. The bucket name is specified in the script.

- [`laser-notif.js`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/Cloud/laser-notif.js): This JavaScript script is a Google Cloud Function that sends a WhatsApp message using the Twilio API whenever the food tank is empty.

- [`laser_notifAndCsv.py`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5stack/laser_notifAndCsv.py) and [`laser_notifAndCsv.m5f`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5stack/laser_notifAndCsv.m5f): These MicroPython script and M5Stack flow files run on M5Stack core2 devices to interact with the laser sensor, and to send HTTP requests to the cloud functions. They do the following:
   - Continuously check the value of the laser reciever.
   - If the laser laser receiver detects the laser beam, it sends a POST request to the `laser-notif.js` cloud function and a POST request to the `laser-csv.py` cloud function.
   
- [`m5_dispenser.py`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5stack/m5_dispenser.py) and [`m5_dispenser.m5f`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5stack/m5_dispenser.m5f`): These Python scripts and M5Stack flow files run on a second M5Stack device to detect movement, send requests to the Flask server, check if a dog was detected from the MQTT feed, run the servo motor, and send a request to the Google Cloud function to write data. They do the following:
   - Continuously check the state of the PIR motion detector, but only when the values of the Adafruit feeds (daily feeding limit and minimum dispensing interval) are respected.
   - If the PIR motion detector detects movement, the m5stack sends a POST request to the Flask server to trigger the webcam and then checks the `dog_detected` feed on Adafruit IO.
   - If a dog is detected by the `webcam.py` script, the `dog_detected` feed will update to `True`. The m5stack will then activate the servo motor to dispense food and will  send a POST request to the `feeding-csv.py` cloud function to store the feeding times. 
 
- [`webcam.py`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/Local/webcam.py): This Python script runs on a local server (e.g., a laptop) and does the following:
   - Captures an image from the webcam whenever it receives a POST request.
   - Uploads the image to a Google Cloud Storage bucket.
   - Calls the Google Vision API to analyze the image and detect if a dog is present.
   - Finally, it publishes a message to the `dog_detected` feed on Adafruit IO. The message will be `True` if a dog is detected and `False` otherwise.

- [`webapp_dispenser.ipynb`](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/WebApp/webapp_dispenser.ipynb): This Google Colab notebook contains the code for the web application, which provides a user interface for visualizing the data, changing dispenser parameters, and computing predictions. It does the following:
   - Flask Server: The Flask server provides three endpoints for fetching the feeding times CSV file, the empty dispenser times CSV file, and the latest image from Google Cloud Storage. These endpoints are used by the Streamlit web application to fetch the necessary data.
   - Streamlit Web Application: The Streamlit script sets up an MQTT client and connects to the Adafruit IO MQTT broker. It displays sliders for setting the daily feeding limit and the minimum dispensing interval, and publishes these values to the respective Adafruit IO feeds. It fetches the feeding times and empty dispenser times CSV files from the Flask API, and plots the data. It also fetches the latest image from the Flask API and displays it. Finally, it computes predictions for the next feeding time and the next empty dispenser time using an ARIMA model.
   - Ngrok: Ngrok is used to expose the local Flask server and the Streamlit web application to the internet. This allows the web application to be accessed from anywhere, not just on the local machine.


## Deployment

This process is divided into nine steps:

1. [**`WhatsApp Notification`**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step1.md): Configuring a Twilio account and a Google Cloud Function to send a WhatsApp notification when the food tank is empty.
2. [**Keep track on Google Cloud Storage**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step2.md): Configuring a Google Cloud Storage bucket and a Google Cloud Function to keep track of when the food tank is empty.
3. [**Set up the M5Stack**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step3.md): Injecting the code into the M5Stack device to handle notifications and CSV file updates related to the laser sensor.
4. [**Feeding Times Cloud Function**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step4.md): Configuring a Google Cloud Function to keep track of when the dog is fed.
5. [**Set up the Adafruit feeds**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step5.md): Creating Adafruit MQTT feeds to communicate with the M5Stack and the Flask servers.
6. [**Image Capture and Analysis**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step6.md): Setting up a Flask server to capture images from the webcam, upload them to Google Cloud Storage, and analyze them to detect if a dog is present.
7. [**Set up the second M5Stack**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step7.md): Injecting the code into the second M5Stack device to detect movement, send requests to the Flask server, check if a dog was detected from the MQTT feed, run the servo motor, and send a request to the Google Cloud function to write data.
8. [**Web Application**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step8.md): Setting up a Streamlit web application to visualize the data, change dispenser parameters, and compute predictions.
9. [**Final Assembly**](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step9.md): Assembling all the hardware components of the Smart Food Dispenser.

## Documents

The Documents folder contains additional resources related to the project:

- [`LinkedIn_Post_Draft.pdf`](https://github.com/stefarine/smart_food_dispenser/blob/main/Documents/LinkdIn_Post_Draft.pdf): A draft for a LinkedIn post about the Smart Food Dispenser project.
- `Project_Overview.md`: A summary of the Smart Food Dispenser project and an explanation of the organization of the files and folders in the repository.
