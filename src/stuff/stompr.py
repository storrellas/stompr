import time
import sys

import stomp

# Global variables
conn = 0
handler_on_connected = 0
handler_on_error = 0
handler_on_message = 0
data = 0

class MyListener(stomp.ConnectionListener):
    def on_connected(self, headers, body):
        print('connected to broker "%s"' % headers)
        global handler_on_connected
        print handler_on_connected
        # handler_on_connected(headers, body)
        global data
        print body
        print headers
        data = headers


    def on_error(self, headers, message):
        print('received an error "%s"' % message)
        global handler_on_error
        # handler_on_error(headers, message)
        print inspect.getargspec(handler_on_connected)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        global handler_on_message
        global data
        # handler_on_message(headers, message)
        data = message

def connection(host, port):
    print('Connecting ...')
    global conn
    conn = stomp.Connection([('localhost','61613')])

def set_listener_on_connected(handler):
    print('Setting on connected handler ...')
    global handler_on_connected
    handler_on_connected = handler

def set_listener_on_error(handler):
    global handler_on_error
    handler_on_error = handler

def set_listener_on_message(handler):
    global handler_on_message
    handler_on_message = handler

def set_listener():
    print('Set Listener ...')
    global conn
    conn.set_listener('', MyListener())

def start():
    global conn
    conn.start()

def connect(user, password):
    global conn
    conn.connect('system', 'manager', wait=True)

def get_data():
    global data

    data_local = data
    data = ''
    return str(data_local)

def subscribe():
    global conn
    conn.subscribe(destination='/queue/test', id=1, ack='auto')

def disconnect(user, destination):
    global conn
    conn.disconnect()
