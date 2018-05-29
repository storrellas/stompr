library(reticulate)
os <- import('os')
py_available()

stomp <- import('stomp')
conn = stomp$Connection(list(tuple('localhost','61613')))
conn$start()
conn$connect('system','manager', wait=TRUE)

#conn$send(body='this is my test', destination='/queue/test')

conn$disconnect()

print("looping forever")
repeat{}
