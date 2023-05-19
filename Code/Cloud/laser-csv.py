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