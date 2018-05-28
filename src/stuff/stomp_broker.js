var http = require("http");
var StompServer = require('stomp-broker-js');

var server = http.createServer();
var stompServer = new StompServer({server: server});

server.listen(61613);

console.log("LFKJSFÑLDJ")

headers = {}
stompServer.subscribe("/**", function(msg, headers) {
  var topic = headers.destination;
  console.log(topic, "->", msg);
}, headers);

stompServer.send('/test', {}, 'testMsg');

console.log("LFKJSFÑLDJ")
