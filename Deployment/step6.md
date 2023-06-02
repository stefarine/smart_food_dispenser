# Step 6: Imamge Capture and Analysis

### In this part we will show you how to set up your portable computer to take pictures from the webcam, send them to a Google Cloud Storage, and analyze them to detect if there is a dog. 

Alternatively, you could use a Bluetooth camera connected to a desktop computer, which can be used as a webcam and conveniently attached to the dispenser. This approach offers the advantage of not requiring the entire computer to be physically present near the dispenser for the script to function.

> Dislaimer: this was done on a Windows computer. but should be possible on a macOS with minor tweaks.

Go the [Google Vision API page](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com) and enable it.

Next, select the three bar menu on the top left and click on `IAM & Admin` > `Service accounts`. 
IMAGE

On the top, click on `Create service account` to create one. On step 1 give it a name, on step 2 greant those required roles: `Storage Object Admin` and `Cloud Vision AI Service Agent`.
IMAGE

Next, click on your newly create service account, and select `keys` from the top menu. Clik on `Add key` and `Create key`, and select the JSON option. This will download your crendentials as as JSON file. Save it safely on your computer.
IMAGE

Now we will show you how to set up the script. Create a new folder on your computer. In this new folder, create a python file and an empty folder to store the pictures. In the python file, paste the following code: 



