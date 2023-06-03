# Smart Food Dispenser

<p align="center">
<img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/39dfd7f3-636c-497f-b9ed-0b117d1bd692">
</p>

## Overview of the project

The aim of this project is to deploy a smart dog food dispenser. The device will allow you to feed your dog while collecting data. You will be able to know how often the animal eats and also to have an eye on its food consumption. Indeed, the device allows you to track how often the container is empty.

The device is able to detect when a dog is in front of it and can serve a portion of food. For this purpose the camera uses a motion detector which, when a movement is detected, triggers the camera. The captured photo is then processed by Google Vision AI, to determine if it is a dog or not. If it is a dog, the device will activate the servo motor to deliver a portion of food. The device will store the date and time of engine activation to keep track of the animal's food consumption.

The device also allows, thanks to a laser emitter and its receiver, to determine when the food tank is empty. Thus, the user will be notified on his phone of the need to refill it. Each time the tank is emptied, the date and time is stored to keep track of the general food consumption of the animal. Also, the user will be able to consult the information about his pet's food consumption through the web app.

<p align="center">
  <img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/ad956444-dc7e-4a02-a683-fea8ec37974b">
  <img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/ad956444-dc7e-4a02-a683-fea8ec37974b">
  <img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/ad956444-dc7e-4a02-a683-fea8ec37974b">
</p>

## Demonstration video

video ici

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
│       ├── laser.m5f
│       ├── laser.py
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
│
└── README.md
```
_*You might 
_**For this project we used a windows computer and its webcam but it is quite possible to use another type of camera that integrates better with the device._
