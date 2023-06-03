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
