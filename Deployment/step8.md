# Step 8 : Setting up the webapp

### In this part we will show you how to set up a webapp that will be able to visualize the data, change dispenser parameters, and compute some predictions. 

Download and open [this file](https://github.com/stefarine/smart_food_dispenser/blob/main/Code/WebApp/webapp_dispenser.ipynb) into any notebooks interface (Jupyter, Google colab, etc). 

1. Run the first cell to install the required packages.

![step8_img2](https://github.com/stefarine/smart_food_dispenser/assets/114418718/89dbed17-07d7-4978-a5bb-f7c4475826ef)

2. Run this second cell and login with your project Google Cloud Account.

![step8_img3](https://github.com/stefarine/smart_food_dispenser/assets/114418718/b3e9cf03-e771-45d0-96fb-a8c0fa5d4c3a)

3. Modify the following line before running the third cell. 

![step8_img4](https://github.com/stefarine/smart_food_dispenser/assets/114418718/ad1a2cb8-7716-473d-8469-bc7790f4019c)

4. Modifify those lines before running the fourth cell. 

![step8_img6](https://github.com/stefarine/smart_food_dispenser/assets/114418718/9eafd2eb-c4bb-4fe7-9c36-9ccfe31442f7)

5. You could now run the webapp locally. But to run it on the web, you will have to create a ngrok account. 
First, go to [ngrok](https://ngrok.com/) and click on sign up for free.
Once you are logged in, click on `Your Authtoken` on the left menu, and copy it. 

![step8_img7](https://github.com/stefarine/smart_food_dispenser/assets/114418718/59ddd35a-d779-4c9c-837d-79dcb96c2449)

  Now go back to the notebook, and copy your authtoken in the fifth cell, replacing `AUTH_TOKEN`. Run the cell. 

![step8_img8](https://github.com/stefarine/smart_food_dispenser/assets/114418718/c69b659f-8010-468a-b135-3842f5507df4)

6. Run the sixth cell. The address to your webapp will be printed, like in the following image. (the address is on the line starting with `Streamlit app running at NgrokTunnel:`. In this case the address is `https://4690-35-199-161-15.ngrok-free.app` but it will change every time you restard the ngrok app. 

![step8_img9](https://github.com/stefarine/smart_food_dispenser/assets/114418718/d4689e03-912d-437f-b8c4-b5c2178d587b)

7. Bonus: if you wish to recieve a sms containing the address of the application to easily open it on your mobile devices, you could use twilio similarly to step 1. First, go to [Twilio](https://www.twilio.com/console).    Login with your account, and on this page click on `Get a phone number`. Next, copy the `Account SID` and `Auth Token` and safely store the values. 
   
![step8_img10](https://github.com/stefarine/smart_food_dispenser/assets/114418718/15955d59-e825-4ba7-9d56-6100466170ec)
   
   Next, on the menu on the left, click on `Phone Numbers` > `Active Numbers` and copy the number on the screen. 
   
![step8_img11](https://github.com/stefarine/smart_food_dispenser/assets/114418718/10d2e7f3-1e71-4a84-9d90-e64610084ba3)

   Once your account is set up, you can go back to the notebook and change those lines in the following cell. If you run it, it well send an sms containing the webapp address to your personal phone number. 

![step8_img12](https://github.com/stefarine/smart_food_dispenser/assets/114418718/6617588b-30b8-470d-92ca-af47041c56dc)

---

Everything is set up! When launched, your webapp will look like this:

![step8_img1](https://github.com/stefarine/smart_food_dispenser/assets/114418718/da6aca1f-a0f9-4e71-8314-7a40bec2093e)


You will be able to visualize the data like the exact feeding times, but also when the dispenser runs out of food. Moreover, it will also provide the latest image captured by the laptop script and offer predictive analytics, such as when your dog is likely to eat next or when the dispenser might need a refill.

Finally, there are sliders on the left-hand side of the screen for setting daily limits and the minimum interval between feedings. Any adjustments made to these settings will alter the MQTT feed, which will be promptly acknowledged by the m5stack.
