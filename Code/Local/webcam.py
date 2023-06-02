from flask import Flask, request
from google.cloud import storage, vision
import os
import glob
from google.oauth2 import service_account
import cv2
import time
import os
from datetime import datetime, timedelta
import logging
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Replace with your Google Cloud project ID
project_id = 'GOOGLE PROJECT ID'
keyfile_path = 'PATH TO JSON FILE'
credentials = service_account.Credentials.from_service_account_file(keyfile_path)

storage_client = storage.Client(project=project_id, credentials=credentials)
vision_client = vision.ImageAnnotatorClient(credentials=credentials)

# Replace with your storage bucket name
bucket_name = 'BUCKET_NAME'
bucket = storage_client.get_bucket(bucket_name)

# Flask server
@app.route('/upload_image', methods=['POST'])
def upload_image():
    
    # Taking a picture
    cap = cv2.VideoCapture(0)
    for _ in range(10):
        ret, frame = cap.read()
        time.sleep(0.1)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # save the frame as an image file
        timestamp = datetime.now()
        filename = timestamp.strftime('%Y%m%d%H%M%S') + '.jpg'
        cv2.imwrite(image_dir + filename, frame)

    # Find the latest picture in the specific folder (replace with the actual folder path)
    folder_path = "PATH TO YOUR IMAGE FOLDER"
    latest_image = max(glob.glob(os.path.join(folder_path, '*.jpg')), key=os.path.getctime)

    # Upload the image to Google Cloud Storage
    image_name = os.path.basename(latest_image)
    blob = bucket.blob(image_name)
    blob.upload_from_filename(latest_image)

    # Call the Google Vision API to recognize patterns in the image
    image_url = f'gs://{bucket_name}/{image_name}'
    image = vision.Image()
    image.source.image_uri = image_url

    response = vision_client.label_detection(image=image)
    labels = response.label_annotations

    # Check if a dog is recognized
    dog_detected = False
    for label in labels:
        print(label)
        if label.description.lower() == 'dog':
            dog_detected = True
            break

    # MQTT
    # Create a logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Create an MQTT client
    client = mqtt.Client()

    # Set the username and password (replace with your own)
    client.username_pw_set('ADAFRUIT_USERNAME', 'ADAFRUIT_KEY')

    # Connect to the Adafruit IO MQTT broker
    logger.info("Connecting to Adafruit IO...")
    client.connect('io.adafruit.com', 1883)

    # Publish a message to the 'dog_detected' feed (replace 'USERNAME' with your own)
    logger.info("Publishing message to 'dog_detected' feed...")
    result = client.publish('USERNAME/feeds/dog_detected', str(dog_detected))
    if result[0] == mqtt.MQTT_ERR_SUCCESS:
        logger.info("Message published successfully")
    else:
        logger.error(f"Failed to publish message: {result}")

    time.sleep(3)
    
    # Disconnect from the broker
    client.disconnect()

    return 'Image processed', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)