# Step 4 : Feeding Times Cloud Function

### In this step we will configure a Google Cloud Function to keep track of the date and time of when the dog is fed. 

The same bucket as step 2 can be used to store this data. Go to [Google Cloud Functions](https://console.cloud.google.com/functions) and create a new function. Configure it and give it a name. Then choose the *Python 3.9* execution environment.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/e23a0a70-1206-449e-9930-b75863aa637d">
</br></br>

Replace the code in main.py with the code below. As before, change "BUCKET_NAME" to the the bucket created in step 2. If you want to change the timezone, you can do that on line 12. Replace what's in the round brackets `tz = timezone('Europe/Paris)` for your preferred timezone available from this [list](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568). The code is also available [here](..)

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

    if request_json and "feed" in request_json:
        feed_value = request_json["feed"]
    elif request_args and "feed" in request_args:
        feed_value = request_args["feed"]
    else:
        return "No value provided"

    csv_file_name = "data.csv"

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
        column_names = "time,feed\n"
    else:
        column_names = ""

    # Append new data with the current time and CO2 value
    new_data = f"{current_time()},{feed_value}\n"
    updated_content = column_names + existing_content + new_data

    # Write the updated content to the CSV file
    blob.upload_from_string(updated_content, content_type="text/csv")
    print(f"Attempting to write to bucket: {bucket_name}")
    print(f"Content to write: {updated_content}")
    return f"Data appended to CSV file '{csv_file_name}' in bucket '{bucket_name}'."
``` 
Then add the following lines to requirements.txt
```
google-cloud-storage
flask
pytz
```

Don't forget to change the name of the entry point to write_csv and then deploy the function.

<img height=450 src="https://github.com/stefarine/smart_food_dispenser/assets/114418718/f2f2726e-618d-4a6d-9dbd-60ec67b1c6b6">

Don't forget to give access to "allUsers" as a Cloud Functions requester as in step 1.</br></br>

You now have a function that is triggered by an HTTP request and writes data to a database. This data is then used to track the dispenser's activity. The next [step](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step5.md) is to set up the Adafruit feeds, which will be used to communicate with the M5Stack and the Flask servers.
