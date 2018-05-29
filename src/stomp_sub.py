import time
import sys

import stomp
import rpy2.robjects as robjects

class MyListener(stomp.ConnectionListener):
    def on_connected(self, headers, body):
        print('connected to broker "%s"' % headers)
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        robjects.r.source('src/script.R');


conn = stomp.Connection([('localhost','61613')])
conn.set_listener('', MyListener())
conn.start()
conn.connect('system', 'manager', wait=True)

conn.subscribe(destination='/queue/test', id=1, ack='auto')

#conn.send(body='this is my test', destination='/queue/test')

# time.sleep(2)
# conn.disconnect()
while True:
    pass
