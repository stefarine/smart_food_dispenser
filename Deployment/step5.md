# Step 5 : Set up the adafruit feeds

### In this part we will show you how to create adafruit mqtt feeds that will be used for later steps.

Go to [io.adafruit](https://io.adafruit.com/) and create a new account.

![step5_image1](https://github.com/stefarine/smart_food_dispenser/assets/114418718/553e38a8-1763-43a3-99ba-51afd2073417)

Once the account is created, click on `IO` on the top menu, then `Feeds`, and then `New Feed`. 

![step5_image2](https://github.com/stefarine/smart_food_dispenser/assets/114418718/56551e33-9ed4-412a-ab6a-c0c7e801b6c8)


Create 3 differents feeds, and name them: `daily_limit`, `dog_detected`	and `min_dispense_interval`.

Next, click on the little key icon and take note of the Username and Active Key values for later use. 

![step5_image3](https://github.com/stefarine/smart_food_dispenser/assets/114418718/fa29e90c-bc27-48bf-89c6-4f70196ada9e)


Now that the Adafruit feeds are set up, you have a system that allows you to send and receive data from the M5Stack and the Flask server. These feeds will be used to control the dispenser's parameters and to communicate the detection of a dog. The next [step](https://github.com/stefarine/smart_food_dispenser/blob/main/Deployment/step6.md) is to set up the image capture and analysis system, which will be responsible for detecting the presence of a dog.
