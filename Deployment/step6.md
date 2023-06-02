# Step 6: Image Capture and Analysis

### In this part we will show you how to set up your portable computer to take pictures from the webcam, send them to a Google Cloud Storage, and analyze them to detect if there is a dog. 

Alternatively, you could use a Bluetooth camera connected to a desktop computer, which can be used as a webcam and conveniently attached to the dispenser. This approach offers the advantage of not requiring the entire computer to be physically present near the dispenser for the script to function.

> Dislaimer: this was done on a Windows computer. but should be possible on a macOS with minor tweaks.

Let's proceed with the steps to enable and configure the Google Vision API:

1. Visit the [Google Vision API page](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com) and enable it for your project.

2. Access the menu on the top left, represented by three horizontal bars, and navigate to `IAM & Admin` > `Service accounts.` 
IMAGE

3. Click on "Create service account" at the top to create a new service account. In "Step 1," provide a name for the service account. For "Step 2," grant the required roles: `Storage Object Admin` and `Cloud Vision AI Service Agent`.
IMAGE

4. Select your newly created service account, and from the top menu, click on `Keys`. Then, click on `Add key`, choose the `Create key` option, and select the JSON format. This will download the credentials as a JSON file. Make sure to securely save the file on your computer. 
IAMGE

Now we will show you how to set up the script. Create a new folder on your computer. In this new folder, create a python file and an empty folder to store the pictures. In the python file, paste the following code: 
```python
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
```
The code is also available [here]https://github.com/stefarine/smart_food_dispenser/blob/main/Code/Local/webcam.py. 
You should do several modifications to the code to work with your own Google Cloud project:
1. Line 16: Replace `GOOGLE PROJECT ID` with your own project id.
```python 
project_id = 'GOOGLE PROJECT ID'
```
2. Line 17: Replace `PATH TO JSON FILE` with the path of the json file you downloaded earlier.
```python 
project_id = 'GOOGLE PROJECT ID'
```
3. Line 24: Replace `BUCKET_NAME` with the name of the bucket you created in step 1.
```python 
bucket_name = 'BUCKET_NAME'
```   
4. Line 46: Replace `PATH TO YOUR IMAGE FOLDER` with the path of the image folder you created earlier.
```python 
folder_path = "PATH TO YOUR IMAGE FOLDER"
```
4. Line 79: Replace `ADAFRUIT_USERNAME` and  `ADAFRUIT_KEY` with the respective values you wrote down on step 5.
```python 
client.username_pw_set('ADAFRUIT_USERNAME', 'ADAFRUIT_KEY')
```  
