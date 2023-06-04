# Project Overview and Folder Structure

This document provides a summary of the Smart Food Dispenser project and explains the organization of the files and folders in the repository.

## Code

The code for the Smart Food Dispenser is divided into several scripts that handle different aspects of the system:

- `feeding-csv.py`: This Python script is a Google Cloud Function that writes the current date and time to a CSV file in a Google Cloud Storage bucket whenever the dog is fed. 

- `laser-csv.py`: This Python script is a Google Cloud Function that writes the current date and time to a CSV file in a Google Cloud Storage bucket whenever the food tank is empty. The bucket name is specified in the script.

- `laser-notif.js`: This JavaScript script is a Google Cloud Function that sends a WhatsApp message using the Twilio API whenever the food tank is empty.

- `laser_notifAndCsv.py` and `laser_notifAndCsv.m5f`: These MicroPython script and M5Stack flow files run on M5Stack core2 devices to interact with the laser sensor, and to send HTTP requests to the cloud functions. They do the following:
   - Continuously check the value of the laser reciever.
   - If the laser laser receiver detects the laser beam, it sends a POST request to the 'laser-notif' cloud function and a POST request to the 'laser-csv' cloud function.
   
- `m5_dispenser.py` and `m5_dispenser.m5f`: These Python scripts and M5Stack flow files run on a second M5Stack device to detect movement, send requests to the Flask server, check if a dog was detected from the MQTT feed, run the servo motor, and send a request tothe Google Cloud function to write data. They do the following:
   - Continuously check the state of the PIR motion detector, but only when the values of the Adafruit feeds (daily feeding limit and minimum dispensing interval) are respected.
   - If the PIR motion detector detects movement, the m5stack sends a POST request to the Flask server to trigger the webcam and then checks the 'dog_detected' feed on Adafruit IO.
   - If a dog is detected by the `webcam.py` script, the `dog_detected` feed will update to `True`. The m5stack will then activate the servo motor to dispense food andwill  send a POST request to the 'feeding-csv.py' cloud function to store the feeding times. 
 
- `webcam.py`: This Python script runs on a local server (e.g., a laptop) and does the following:
   - Captures an image from the webcam whenever it receives a POST request.
   - Uploads the image to a Google Cloud Storage bucket.
   - Calls the Google Vision API to analyze the image and detect if a dog is present.
   - If a dog is detected, it publishes a message to the 'dog_detected' feed on Adafruit IO.

- `webapp_dispenser.ipynb`: This Jupyter notebook contains the code for the Streamlit web application, which provides a user interface for visualizing the data, changing dispenser parameters, and computing predictions. It does the following:
   - Sets up an MQTT client and connects to the Adafruit IO MQTT broker.
   - Displays sliders for setting the daily feeding limit and the minimum dispensing interval, and publishes these values to the respective Adafruit IO feeds.
   - Fetches the feeding times and empty dispenser times CSV files from the Flask API, and plots the data.
   - Fetches the latest image from the Flask API and displays it.
   - Computes predictions for the next feeding time and the next empty dispenser time using an ARIMA model.





## Deployment

The deployment process involves setting up and configuring all the hardware and software components, injecting the code into the M5Stack devices, and setting up a web application to visualize the data and control the dispenser's parameters. The process is divided into nine steps:

1. **WhatsApp Notification**: Configuring a Twilio account and a Google Cloud Function to send a WhatsApp notification when the food tank is empty.
2. **Keep track on Google Cloud Storage**: Configuring a Google Cloud Storage bucket and a Google Cloud Function to keep track of when the food tank is empty.
3. **Set up the M5Stack**: Injecting the code into the M5Stack device to handle notifications and CSV file updates related to the laser sensor.
4. **Feeding Times Cloud Function**: Configuring a Google Cloud Function to keep track of when the dog is fed.
5. **Set up the Adafruit feeds**: Creating Adafruit MQTT feeds to communicate with the M5Stack and the Flask servers.
6. **Image Capture and Analysis**: Setting up a Flask server to capture images from the webcam, upload them to Google Cloud Storage, and analyze them to detect if a dog is present.
7. **Set up the second M5Stack**: Injecting the code into the second M5Stack device to detect movement, send requests to the Flask server, check if a dog was detected from the MQTT feed, run the servo motor, and send a request to the Google Cloud function to write data.
8. **Web Application**: Setting up a Streamlit web application to visualize the data, change dispenser parameters, and compute predictions.
9. **Final Assembly**: Assembling all the hardware components of the Smart Food Dispenser.

## Documents

The Documents folder contains additional resources related to the project:

- `LinkedIn_Post_Draft.pdf`: A draft for a LinkedIn post about the Smart Food Dispenser project.
- `Project_Overview.md`:
