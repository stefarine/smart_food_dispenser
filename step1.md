# Laser truc blabla

##In this step we will configure a twilio account and a Google cloud function so that the m5Stack is able to send a notification on WhatsApp when the food tank is empty.

Go to [Twilio](https://www.twilio.com/en-us) and create a free account and set up your account. Then, go to the console and request a Twilio Number. Just press the button as shown in the picture below and the number will be assigned to you.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/4dc4dd18-a810-4ef0-a663-1dc3f030f8f1">
</br></br>

Then in the menu on the left side of the screen, you have to go to **Develop > Messaging > Try it out > Send a WhatsApp message**

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/51dad0a0-61ab-425e-9359-dae9883200b7">
</br></br>

You will then have to scan the qr code displayed with the phone that has the number you used to set up your Twilio account. This will open a Whatsapp conversation for you. Just confirm the message and add the number to your contacts.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/acea5cd9-4e1e-4025-a26e-998e24b01416">
<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/a028a2a8-1bea-4a2b-b827-ba821736592a">
</br></br>

Your Twilio account is now configured. Now you have to configure a Google Cloud Function. To do this, go to the Google Cloud Function page after first creating a Google Cloud account and creating a project. Then press the **create a function** button.

<img height=200 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/dd4f3ee6-42f4-44a9-9b82-dce23307b635">
</br></br>

Configure the function as you wish, change its name. Select Node.js 18 and then delete all the code in *index.js* and copy/paste the code below instead. A copy of the code is available [here](Code/Cloud/laser-notif.js). Don't forget to replace the four variables between [] with your variables.


```javascript I'm index.js
const accountSid = [YOUR ACCOUNT SID] ;
const authToken = [YOUR AUTH TOKEN] ;
const client = require('twilio')(accountSid, authToken);

exports.helloWorld = (req, res) => {

  let message = req.query.message || req.body.message || 'yo99o!';
  res.status(200).send(message);

    client.messages
        .create({
            body: 'Il faut remettre des croquettes',
            from: 'whatsapp:[YOUR TWILIO NUMBER]',
            to: 'whatsapp:[YOUR REAL NUMBER]'
        })
        .then(message => console.log(message.sid))
        .done();
};
```

Also replace the code in *package.json* by the code below to have the necessary dependencies.
```javascript I'm package.json
{
  "name": "sample-http",
  "version": "0.0.1",
  "dependencies": {
    "twilio": "^4.10.0"
  }
}
```
All you have to do now is press the deploy button and wait a few minutes for the function to be deployed. Once the function is correctly deployed, go to its page and in the section trigger copy the triggering URL. Keep the URL somewhere for now.

<img height=350 src="https://github.com/stefarine/smart_food_dispenser/assets/57952280/d8a95ad9-b1b0-458f-91b9-1135c818216e">

