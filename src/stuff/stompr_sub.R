library(reticulate)
os <- import('os')
py_available()

stompr <- import_from_path('stompr', path='/vagrant/workspace/stompr/src/stuff/')

on_connected <- function(headers, body){
    print('handler - connected to broker')
}

on_error <- function(headers){
    print('handler - received an error')
}

on_message <- function(headers){
    print('handler - received message')
}


stompr$connection('localhost', '61613')
stompr$set_listener_on_connected(on_connected)
stompr$set_listener_on_error(on_error)
stompr$set_listener_on_message(on_message)
stompr$set_listener()
stompr$start()
stompr$connect('system', 'manager')
stompr$subscribe()

# conn = stomp$Connection(list(tuple('localhost','61613')))
# conn$start()
# conn$connect('system','manager', wait=TRUE)
#
# #conn$send(body='this is my test', destination='/queue/test')
#
# conn$disconnect()
#
print("looping forever")
repeat{}
