import time
import sys

import stomp

# Global variables
conn = 0

class StompRListener(stomp.ConnectionListener):

    data = 0

    def get_data(self):
        data_local = self.data
        self.data = ''
        return str(data_local)

    def on_connected(self, headers, body):
        print('connected to broker "%s"' % headers)
        self.data = headers

    def on_error(self, headers, message):
        print('received an error "%s"' % message)
        self.data = message

    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        self.data = message

# Generate listener object
listener = StompRListener()

def connection(host, port):
    print('Connecting ...')
    global conn
    conn = stomp.Connection([('localhost','61613')])

def set_listener():
    print('Set Listener ...')
    global conn
    #conn.set_listener('', StompRListener())
    conn.set_listener('', listener)


def start():
    global conn
    conn.start()

def connect(user, password):
    global conn
    conn.connect('system', 'manager', wait=True)

def get_data():
    return listener.get_data()
    # global data
    #
    # data_local = data
    # data = ''
    # return str(data_local)

def subscribe():
    global conn
    conn.subscribe(destination='/queue/test', id=1, ack='auto')

def disconnect(user, destination):
    global conn
    conn.disconnect()
