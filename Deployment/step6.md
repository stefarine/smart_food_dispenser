# Step 6: Imamge Capture and Analysis

### In this part we will show you how to set up your portable computer to take pictures from the webcam, send them to a Google Cloud Storage, and analyze them to detect if there is a dog. 

Alternatively, you could use a Bluetooth camera connected to a desktop computer, which can be used as a webcam and conveniently attached to the dispenser. This approach offers the advantage of not requiring the entire computer to be physically present near the dispenser for the script to function.

> Dislaimer: this was done on a Windows computer. but should be possible on a macOS with minor tweaks.

Let's proceed with the steps to enable and configure the Google Vision API:

1. Visit the [Google Vision API page](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com) and enable it for your project.

2. Access the menu on the top left, represented by three horizontal bars, and navigate to "IAM & Admin" > "Service accounts." 
IMAGE

3. Click on "Create service account" at the top to create a new service account. In "Step 1," provide a name for the service account. For "Step 2," grant the required roles: "Storage Object Admin" and "Cloud Vision AI Service Agent."
IMAGE

4. Select your newly created service account, and from the top menu, click on "Keys." Then, click on "Add key," choose the "Create key" option, and select the JSON format. This will download the credentials as a JSON file. Make sure to securely save the file on your computer. 
IAMGE

Now we will show you how to set up the script. Create a new folder on your computer. In this new folder, create a python file and an empty folder to store the pictures. In the python file, paste the following code: 
