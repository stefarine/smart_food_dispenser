# Step 2 : Keep track on google cloud storage

### In this step we will configure a bucket on Google Cloud Storage and a Google Cloud Function to keep track of the date and time of when the food tank is empty.

To start, activate Google Cloud Storage on the same project as in step 1 and create a new Bucket like in the image below. Configure the bucket as you like and choose a name.

<img height=250 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/2e31b194-3750-479e-bf15-3c2cbe29ae21">
</br></br>

Then go to google cloud function and create a new function. Configure it and give it a name. Then choose the *Python 3.9* execution environment.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/e23a0a70-1206-449e-9930-b75863aa637d">
</br></br>

Replace the code in *main.py* with the code below. Be sure to change the name of the bucket and put the name of the bucket previously created. The code is also available [here](../Code/Cloud/laser-csv.py).

```python 
import os
import csv
from flask import escape, request
from google.cloud import storage
from datetime import datetime
from pytz import timezone

storage_client = storage.Client()
bucket_name = os.environ.get("BUCKET_NAME")

def current_time():
    tz = timezone('Europe/Paris')
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

def write_csv(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "laser" in request_json:
        data = request_json["laser"]
    elif request_args and "laser" in request_args:
        data = request_args["laser"]
    else:
        return "No data provided"

    csv_file_name = "data_laser.csv"

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(csv_file_name)
    
    # Read the existing content of the CSV file
    try:
        existing_content = blob.download_as_text()
        first_time = False
    except Exception as e:
        print(f"Error downloading existing content: {e}")
        existing_content = ""
        first_time = True

    # Write column names if it's the first time creating the CSV file
    if first_time:
        column_names = "time,empty\n"
    else:
        column_names = ""

    # Append new data with the current time
    new_data = f"{current_time()},{data}\n"
    updated_content = column_names + existing_content + new_data
    
    # Write the updated content to the CSV file
    blob.upload_from_string(updated_content, content_type="text/csv")
    print(f"Attempting to write to bucket: {bucket_name}")
    print(f"Content to write: {updated_content}")
    return f"Data appended to CSV file '{csv_file_name}' in bucket '{bucket_name}'."
```
Then add the following lines to *requirements.txt*


```python I'm requirements.txt
google-cloud-storage
flask
pytz

```
Don't forget to change the name of the entry point to write_csv and then deploy the function.

<img height=450 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/6d3ba8c0-a7b3-4572-a7ea-48a3c27de23a">
</br></br>
Don't forget to give access to "allUsers" as a Cloud Functions requester as in step 1.</br></br>

At this point, we have set up Twilio and Google cloud function in step 1 to notify us when the kibble tank is empty. Then, in step 2, we set google cloud storage and google cloud function to write in a csv when the tank is empty. In [step 3](step3.md) we will run the code on the first m5stack to handle all this.
