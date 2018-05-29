var Stomp = require('stompjs');
var client = Stomp.overWS('ws://localhost:61614/stomp');
var R = require("./r-script/index.js");


var connect_callback = function() {
  // called back after the client is connected and authenticated to the STOMP server
  console.log("connect callback")

  // Subscribe
  var subscription = client.subscribe('/queue/test', function(message){
    console.log("++ Received message ++")
    console.log(message)

    var out = R("src/script.R")
//      .data("hello world", 20)
      .callSync();
    console.log(out);
  });

};

var error_callback = function(error) {
  // display the error's message header:
  console.log("error callback")
};

client.connect('system', 'manager', connect_callback, error_callback);
/**/
