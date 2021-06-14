//Python server side code
import socket
import sys
# creating a socket object 
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket object has been created 
print("Socket has successfully created")
# We need to pass an empty string so that all host interfaces are available 
HOST = "
# let us reserve a port which we can open 
PORT = 8080
# let us bind our socket object that particular port
try:
  mySocket.bind((HOST, PORT)) 
  except socket.error as msg:
    print('Binding has failed. Error Code is : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print("Socket object is bound to the port ", PORT) 
# putting the socket into listening mode 
mySocket.listen(10)
print("Socket is listening")
while True: 
  c, addr = mySocket.accept()
  print("Got connection from ", addr)
