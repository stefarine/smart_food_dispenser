# Step 2 : Keep track on google cloud storage

### In this step we will configure a bucket on Google Cloud Storage and a Google Cloud Function to keep track of the date and time of when the food tank is empty.

To start, activate Google Cloud Storage on the same project as in step 1 and create a new Bucket like in the image below. Configure the bucket as you like and choose a name.

<img height=250 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/2e31b194-3750-479e-bf15-3c2cbe29ae21">
</br></br>

Then go to google cloud function and create a new function. Configure it and give it a name. Then choose the *Python 3.9* execution environment.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/e23a0a70-1206-449e-9930-b75863aa637d">
</br></br>

Replace the code in *main.py* with the code below. Be sure to change the name of the bucket and put the name of the bucket previously created. The code is also available [here](../Code/Cloud/laser-csv.py).

```python I'm main.py
import os
import csv
from flask import escape, request
from google.cloud import storage

storage_client = storage.Client()
bucket_name = os.environ.get("BUCKET_NAME")

def write_csv(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "data" in request_json:
        data = request_json["data"]
    elif request_args and "data" in request_args:
        data = request_args["data"]
    else:
        return "No data provided"

    csv_file_name = "data.csv"

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(csv_file_name)

    csv_content = ""
    for row in data:
        csv_content += ",".join(map(str, row)) + "\n"

    blob.upload_from_string(csv_content, content_type="text/csv")

    return f"CSV file '{csv_file_name}' created in bucket '{bucket_name}'."
```
Then add the following lines to *requirements.txt*


```python I'm requirements.txt
google-cloud-storage
flask

```
