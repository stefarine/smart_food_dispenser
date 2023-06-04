# Smart Food Dispenser

<p align="center">
<img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/39dfd7f3-636c-497f-b9ed-0b117d1bd692">
</p>

## Overview of the project

The aim of this project is to deploy a smart dog food dispenser. The device will allow you to feed your dog while collecting data. You will be able to know how often the animal eats and also to have an eye on its food consumption. Indeed, the device allows you to track how often the container is empty.

The smart dispenser uses a combination of a motion detector and a camera to identify when your dog is present. When motion is detected, the camera captures an image, which is then analyzed by the Google Vision API to determine whether a dog is in the frame. If a dog is detected, the dispenser activates a servo motor to dispense a portion of food. The date and time of each feeding event are logged, allowing you to track your pet's feeding times and frequency.

The device also allows, thanks to a laser emitter and its receiver, to determine when the food tank is empty. Thus, the user will be notified on his phone of the need to refill it. Each time the tank is emptied, the date and time is stored to keep track of the general food consumption of the animal. 

Finally, the user will be able to access a web application that allow them to view their pet's feeding and empty dispenser logs, adjust the dispenser's settings, and view predictions about future feeding times and empty dispenser events

<p align="center">
  <img height=300 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/d48da7a2-96c2-40ad-a09d-d163a3620da6">
  <img height=300 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/ad956444-dc7e-4a02-a683-fea8ec37974b">
  <img height=300 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/a52f4d9c-2f0d-4bfa-910a-28dbccf2476a">
</p>


## Demonstration video 📺

[![vid](https://img.youtube.com/vi/JJP4o6CnbYs/0.jpg)](https://www.youtube.com/watch?v=JJP4o6CnbYs)

[https://www.youtube.com/watch?v=JJP4o6CnbYs](https://www.youtube.com/watch?v=JJP4o6CnbYs)

## Requirements

To deploy this project you will need the following material : 

- 2x [M5Stack Core2](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)*
- [Laser.tx unit](https://shop.m5stack.com/products/laser-tx-unit)
- [Laser.rx unit](https://shop.m5stack.com/products/laser-rx-unit)
- [Servo kit 360°](https://shop.m5stack.com/products/servo-kit-360)
- [Motion sensor](https://shop.m5stack.com/products/pir-module)
- A computer and its webcam**
- A 3D printer or some DIY skills

## Deployment

You will find in the folder [deployment](Deployment) the different steps to realize this project. To start, go to [step 1](Deployment/step1.md).

## Repository structure
```
│
├── Code
│   ├── Cloud
│   │   ├── feeding-csv.py
│   │   ├── laser-csv.py
│   │   └── laser-notif.js
│   ├── Local
│   │   └── webcam.py
│   ├── WebApp
│   │   └── webapp_dispenser.ipynb
│   └── m5Stack
│       ├── laser_notifAndCsv.py
│       └── laser_notifAndCsv.m5f
│       └── m5_dispenser.m5f
│       └── m5_dispenser.py
│
├── Deployment
│   ├── step1.md
│   ├── step2.md
│   ├── step3.md
│   ├── step4.md
│   ├── step5.md
│   ├── step6.md
│   ├── step7.md
│   └── step8.md
│   └── step9.md
│
└── README.md
```
_*It might be possible to use a single M5Stack Core2. This would require adding a compatible GPIO splitter to accommodate the additional sensor connections. Please note, however, that this modification would also necessitate alterations to the code, and the power output of the M5Stack Core2 might not be sufficient to support all connected devices._

_**For this project we used a windows computer and its webcam but it is quite possible to use another type of camera that integrates better with the device._
