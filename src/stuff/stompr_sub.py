import time
import sys

import stompr


def on_connected(headers, body):
    print('handler - connected to broker "%s"' % headers)

def on_error(headers, message):
    print('handler - received an error "%s"' % message)

def on_message(headers, message):
    print('handler - received a message "%s"' % message)


stompr.connection('localhost', '61613')
stompr.set_listener_on_connected(on_connected)
stompr.set_listener_on_error(on_error)
stompr.set_listener_on_message(on_message)
stompr.set_listener()
stompr.start()
stompr.connect('system', 'manager')
stompr.subscribe()

while True:
    pass
