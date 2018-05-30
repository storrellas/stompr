import time
import sys

import stomp

import threading

cv = threading.Condition()
cv.acquire()
cv.notifyAll()
cv.release()

# Generic listener for StompR
class StompRListener(stomp.ConnectionListener):

    data = 0

    def get_data(self):
        global cv
        data_local = self.data
        self.data = ''
        return str(data_local)

    def on_connected(self, headers, body):
        print('connected to broker "%s"' % headers)
        self.data = headers

        # Synchronised block
        global cv
        cv.acquire()
        cv.notifyAll()
        cv.release()

    def on_error(self, headers, message):
        print('received an error "%s"' % message)
        self.data = message

        # Synchronised block
        global cv
        cv.acquire()
        cv.notifyAll()
        cv.release()

    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        self.data = message

        # Synchronised block
        global cv
        cv.acquire()
        cv.notifyAll()
        cv.release()

# Generate global variables
conn = 0
listener = StompRListener()

def connection(host, port):
    print('Connecting ...')
    global conn
    conn = stomp.Connection([('localhost','61613')])

def set_listener():
    global conn
    conn.set_listener('', listener)

def start():
    global conn
    conn.start()

def connect(user, password):
    global conn

    # Synchronised block
    cv.acquire()
    conn.connect('system', 'manager', wait=True)
    cv.wait()
    cv.release()

def read_polling():
    return listener.get_data()

def read_blocking():
    cv.acquire()
    cv.wait()
    cv.release()
    return listener.get_data()

def subscribe():
    global conn
    conn.subscribe(destination='/queue/test', id=1, ack='auto')

def disconnect(user, destination):
    global conn
    conn.disconnect()
