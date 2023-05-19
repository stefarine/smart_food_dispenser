
<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/c15d3141-0ae9-4a2c-8162-5765028076e7">
</br></br>

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
