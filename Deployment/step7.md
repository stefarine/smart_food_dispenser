# Step 7 : Set up the second m5stack

### In this part we will simply inject the code into the m5stack so that it can detect movement, send requests to the flask server set up in step 6, checking if a dog was detected from the MQTT feed, running the servo motor, and sending a request to the Google Cloud function to write data.

First of all, connect your servo motor to port C and your PIR motion detector to port B.
Go to [flow.m5stack](https://flow.m5stack.com/). Now you have two choices. Either you import [this file](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5Stack/m5_dispenser.m5f) or you paste [this code](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/m5Stack/m5_dispenser.py). 
But in both cases you will have the following modifications:

### UIFlow Blockly
![step7_image1](https://github.com/stefarine/smart_food_dispenser/assets/114418718/c060e590-4a7f-4f04-8c60-d7449184db10)
### Micropython
```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from m5mqtt import M5mqtt
import ntptime
import urequests
import time
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
servo_0 = unit.get(unit.SERVO, unit.PORTC)
pir_0 = unit.get(unit.PIR, unit.PORTB)


min_dispense_interval = None
dog_detected = None
daily_limit = None
dispense_count = None
last_reset_day = None
last_dispense_time = None



label2 = M5Label('label2', x=220, y=23, color=0x000, font=FONT_MONT_14, parent=None)
label4 = M5Label('label4', x=220, y=45, color=0x000, font=FONT_MONT_14, parent=None)
label3 = M5Label('label3', x=220, y=75, color=0x000, font=FONT_MONT_14, parent=None)
label5 = M5Label('Dispense count today:', x=3, y=103, color=0x000, font=FONT_MONT_14, parent=None)
motion_detection2 = M5Label('loading...', x=220, y=172, color=0x000, font=FONT_MONT_18, parent=None)
label8 = M5Label('Minutes since last feeding:', x=3, y=75, color=0x000, font=FONT_MONT_14, parent=None)
dog_detected_label2 = M5Label('loading...', x=220, y=208, color=0x000, font=FONT_MONT_18, parent=None)
label9 = M5Label('Min dispense interval:', x=3, y=23, color=0x000, font=FONT_MONT_14, parent=None)
label0 = M5Label('Detected movement:', x=3, y=172, color=0x000, font=FONT_MONT_18, parent=None)
label7 = M5Label('label7', x=220, y=103, color=0x000, font=FONT_MONT_14, parent=None)
label10 = M5Label('Daily limit:', x=3, y=45, color=0x000, font=FONT_MONT_14, parent=None)
label11 = M5Label('Current day cycle:', x=3, y=1, color=0x000, font=FONT_MONT_14, parent=None)
line0 = M5Line(x1=0, y1=66, x2=325, y2=66, color=0x0051ff, width=1, parent=None)
line1 = M5Line(x1=-1, y1=124, x2=325, y2=124, color=0x0051ff, width=1, parent=None)
label1 = M5Label('Detected dog: ', x=3, y=208, color=0x000, font=FONT_MONT_18, parent=None)
label12 = M5Label('label12', x=220, y=1, color=0x000, font=FONT_MONT_14, parent=None)
M = M5Label('Motion Detector:', x=3, y=140, color=0x000, font=FONT_MONT_18, parent=None)
label6 = M5Label('label6', x=220, y=140, color=0x000, font=FONT_MONT_14, parent=None)

from numbers import Number



def fun_ADAFRUIT_USERNAME_feeds_min_dispense_interval_(topic_data):
  global min_dispense_interval, dog_detected, daily_limit, dispense_count, last_reset_day, last_dispense_time
  min_dispense_interval = topic_data
  pass

def fun_ADAFRUIT_USERNAME_feeds_dog_detected_(topic_data):
  global min_dispense_interval, dog_detected, daily_limit, dispense_count, last_reset_day, last_dispense_time
  dog_detected = topic_data
  pass

def fun_ADAFRUIT_USERNAME_feeds_daily_limit_(topic_data):
  global min_dispense_interval, dog_detected, daily_limit, dispense_count, last_reset_day, last_dispense_time
  daily_limit = int(topic_data)
  pass


m5mqtt = M5mqtt('M5StackCore2', 'io.adafruit.com', 1883, 'ADAFRUIT_USERNAME', 'ADAFRUIT_KEY', 300)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/min-dispense-interval'), fun_ADAFRUIT_USERNAME_feeds_min_dispense_interval_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/dog-detected'), fun_ADAFRUIT_USERNAME_feeds_dog_detected_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/daily-limit'), fun_ADAFRUIT_USERNAME_feeds_daily_limit_)
m5mqtt.start()
ntp = ntptime.client(host='de.pool.ntp.org', timezone=2)
dispense_count = 0
last_reset_day = ntp.formatDate('-')
min_dispense_interval = 100
last_dispense_time = 0
daily_limit = 3
while True:
  label3.set_text(str(((ntp.getTimestamp()) - last_dispense_time) / 60))
  label2.set_text(str(min_dispense_interval))
  label4.set_text(str(daily_limit))
  label7.set_text(str(dispense_count))
  label12.set_text(str(last_reset_day))
  if last_reset_day != (ntp.formatDate('-')):
    dispense_count = 0
    last_reset_day = ntp.formatDate('-')
  if ((ntp.getTimestamp()) - last_dispense_time) / 60 > float(min_dispense_interval):
    if dispense_count < daily_limit:
      label6.set_text('Running')
      label6.set_text_color(0x33ff33)
      if (pir_0.state) == 1:
        motion_detection2.set_text('True')
        motion_detection2.set_text_color(0x33ff33)
        try:
          req = urequests.request(method='POST', url='http://FLASK_IP/upload_image',json={}, headers={})
          gc.collect()
          req.close()
        except:
          pass
        wait(1)
        if dog_detected == 'True':
          dog_detected_label2.set_text('True')
          dog_detected_label2.set_text_color(0x33ff33)
          dispense_count = (dispense_count if isinstance(dispense_count, Number) else 0) + 1
          last_dispense_time = ntp.getTimestamp()
          servo_0.write_angle(80)
          wait(3)
          servo_0.write_angle(90)
          try:
            req = urequests.request(method='POST', url='google_function_trigger_url',json={'feed':'1'}, headers={})
            gc.collect()
            req.close()
          except:
            pass
        else:
          dog_detected_label2.set_text('False')
          dog_detected_label2.set_text_color(0xff0000)
          wait(1)
      else:
        motion_detection2.set_text('False')
        motion_detection2.set_text_color(0xff0000)
    else:
      label6.set_text('Not Running')
      label6.set_text_color(0xff0000)
      motion_detection2.set_text_color(0x000000)
      motion_detection2.set_text('loading...')
  else:
    label6.set_text('Not Running')
    label6.set_text_color(0xff0000)
    motion_detection2.set_text('loading...')
    motion_detection2.set_text_color(0x000000)
  dog_detected_label2.set_text('loading...')
  dog_detected_label2.set_text_color(0x000000)
  wait_ms(2)

1. On line 66, replace `ADAFRUIT_USERNAME` and `ADAFRUIT_KEY` with the respective values you wrote down on step 5.
```
Here are the modifications to the code:
1. On lines 66, 67, 68 and 69: Replace `ADAFRUIT_USERNAME` and `ADAFRUIT_KEY` with the respective values you wrote down on step 5.
```python
m5mqtt = M5mqtt('M5StackCore2', 'io.adafruit.com', 1883, 'ADAFRUIT_USERNAME', 'ADAFRUIT_KEY', 300)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/min-dispense-interval'), fun_Giac_feeds_min_dispense_interval_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/dog-detected'), fun_Giac_feeds_dog_detected_)
m5mqtt.subscribe(str('ADAFRUIT_USERNAME/feeds/daily-limit'), fun_Giac_feeds_daily_limit_)
```
2. On line 94, replace  `FLASK_IP` with the flask IP address you wrote down in step 6.
```python
req = urequests.request(method='POST', url='http://FLASK_IP/upload_image',json={}, headers={})
```
3. On line 109, replace  `cloud_function_trigger` with the Google Cloud Function trigger URL from step 4. 
```python
 req = urequests.request(method='POST', url='cloud_function_trigger',json={}, headers={})
 ```
 
