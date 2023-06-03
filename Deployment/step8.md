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

Now go back to the notebook, and copy your authtoken in the fifth cell, replacing `AUTH_TOKEN`

![step8_img8](https://github.com/stefarine/smart_food_dispenser/assets/114418718/c69b659f-8010-468a-b135-3842f5507df4)


![step8_img1](https://github.com/stefarine/smart_food_dispenser/assets/114418718/da6aca1f-a0f9-4e71-8314-7a40bec2093e)
