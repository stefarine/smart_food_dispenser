# Step 7 : Set up the second m5stack

### In this part we will simply inject the code into the m5stack so that it can detect movement, send requests to the flask server set up in step 6, checking if a dog was detected from the MQTT feed, running the servo motor, and sending a request to the Google Cloud function to write data.

First of all, connect your servo motor to port C and your PIR motion detector to port B.
Go to [flow.m5stack](https://flow.m5stack.com/). Now you have two choices. Either you import [this file]() or you paster [this code](). 
But in both cases you will have to do some modifications. 

1. On line 66, replace `ADAFRUIT_USERNAME` and `ADAFRUIT_KEY` with the respective values you wrote down on step 5.
```python
m5mqtt = M5mqtt('M5StackCore2', 'io.adafruit.com', 1883, 'ADAFRUIT_USERNAME', 'ADAFRUIT_KEY', 300)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/min-dispense-interval'), fun_Giac_feeds_min_dispense_interval_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/dog-detected'), fun_Giac_feeds_dog_detected_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/daily-limit'), fun_Giac_feeds_daily_limit_)
```
2. On line x, replace  `FLASK_IP` with the adress you wrote down in step 6.
```python
req = urequests.request(method='POST', url='http://FLASK_IP/upload_image',json={}, headers={})
```
3. On line x, replace  `cloud_function_trigger` with the Google Cloud Function trigger adress from step 4. Remember to keep `feed=1` after your adress.
```python
 req = urequests.request(method='POST', url='cloud_function_trigger?feed=1',json={}, headers={})
 ```
 
