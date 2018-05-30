library(reticulate)
os <- import('os')
py_available()

stompr <- import_from_path('stompr', path='/vagrant/workspace/stompr/src/stuff/')

# Configure StompR
stompr$connection('localhost', '61613')
stompr$set_listener()
stompr$start()
stompr$connect('system', 'manager')
stompr$subscribe()

# Polling for data
print("looping forever")
repeat{

  # # Read polling version
  data <- stompr$read_polling()
  if (data == ''){
    # Do nothing
  }else{
    message(sprintf("Published message -> %s\n", data))
  }

  # # Read blocking version
  # data <- stompr$read_blocking()
  # message(sprintf("Got published message -> %s\n", data))

  # Wait for some time
  Sys.sleep(0.5)
}
