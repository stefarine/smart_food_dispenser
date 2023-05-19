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