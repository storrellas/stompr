var Stomp = require('stompjs');
var client = Stomp.overWS('ws://localhost:61614/stomp');


var connect_callback = function() {
  // called back after the client is connected and authenticated to the STOMP server
  console.log("connect callback")

  // Subscribe
  var subscription = client.subscribe('/queue/test', function(message){
    console.log("++ Received message ++")
    console.log(message)
  });

  // Send message
  // start the transaction
  var tx = client.begin();
  // send the message in a transaction
  client.send("/queue/test", {transaction: tx.id}, "message in a transaction");
  // commit the transaction to effectively send the message
  tx.commit();

};

var error_callback = function(error) {
  // display the error's message header:
  console.log("error callback")
};


client.connect('system', 'manager', connect_callback, error_callback);

/*
function message_callback(body, headers) {
    console.log('Message Callback Fired!');
    console.log('Headers: ' + sys.inspect(headers));
    console.log('Body: ' + body);
}

client.on('connected', function() {
    client.subscribe(headers, message_callback);
    console.log('Connected');
});
/**/
