# Step 3 : Set up the m5stack

### In this part we will simply inject the code into the m5stack so that it is ready to notify and write to the CSV when the tank is empty.

Now that everything has been configured in the 2 previous steps, you just need to inject the code into the m5stack. First of all, connect your RX laser module to port B and your TX laser module to port C.</br></br>

Go to [flow.m5stack](https://flow.m5stack.com/). Now you have two choices. Either you import [this file](../Code/m5Stack/laser_notifAndCsv.m5f) and modify both URLs as shown in the image below. The first URL is the one we copied at the end of step 1. The second is to be retrieved in the same way with the Google Cloud Function created in step 2.</br></br>


<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/c15d3141-0ae9-4a2c-8162-5765028076e7">
</br></br>
The second option is simply to copy and paste the code below on flow.m5stack. Don't forget to change the URLs.</br></br>

```python I'm main.py
from m5stack import *
from m5stack_ui import *
from uiflow import *
import urequests
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
laser_tx_0 = unit.get(unit.LASERTX, unit.PORTB)
laser_rx_2 = unit.get(unit.LASERRX, unit.PORTC)


counter = None



label0 = M5Label('label0', x=116, y=72, color=0x000, font=FONT_MONT_14, parent=None)
on = M5Label('on', x=59, y=213, color=0x0a7917, font=FONT_MONT_14, parent=None)
label3 = M5Label('label3', x=236, y=165, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('off', x=142, y=209, color=0xea0e0e, font=FONT_MONT_14, parent=None)
label2 = M5Label('label2', x=229, y=133, color=0x000, font=FONT_MONT_14, parent=None)

from numbers import Number



def buttonB_wasPressed():
  global counter
  laser_tx_0.off()
  label0.set_text(str(laser_rx_2.value()))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global counter
  laser_tx_0.on()
  label0.set_text(str(laser_rx_2.value()))
  pass
btnA.wasPressed(buttonA_wasPressed)


counter = 0
laser_tx_0.on()
while True:
  label0.set_text(str(laser_rx_2.value()))
  if laser_rx_2.value():
    counter = (counter if isinstance(counter, Number) else 0) + 1
    if counter == 1:
      try:
        req = urequests.request(method='GET', url='[YOUR URL]', headers={})
        label2.set_text('okk')
        gc.collect()
        req.close()
      except:
        label2.set_text('Notttt')
      try:
        req = urequests.request(method='POST', url='[YOUR URL]',json={'laser':'laser'}, headers={})
        label3.set_text('okk')
        gc.collect()
        req.close()
      except:
        label3.set_text('Notttt')
  if not (laser_rx_2.value()):
    counter = 0
  wait_ms(2)

```

Congratulations! Now you have a system that allows you to control when the food tank is empty. We will see later how to install it.In the next step we will see how to deploy the motion sensor, the camera and the motor.
