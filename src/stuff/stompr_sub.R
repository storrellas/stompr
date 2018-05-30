library(reticulate)
os <- import('os')
py_available()

stompr <- import_from_path('stompr', path='/vagrant/workspace/stompr/src/stuff/')

on_connected <- py_func(function(headers, body){
    print('handler - connected to broker')
})

on_error <- py_func(function(headers){
    print('handler - received an error')
    return(headers)
})

on_message <- py_func(function(headers){
    print('handler - received message')
    return(headers)
})


stompr$connection('localhost', '61613')
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
repeat{
  data <- stompr$get_data()
  if (data == ''){
    # Do nothing
  }else{
    message(sprintf("Current working dir: %s\n", data))
  }



  #print(paste0("Current working dir: ", data))
  Sys.sleep(0.5)
}
