# Python code of storing the data about clients
# a very simple TCP Client Server in Python that will listen to a certain port importing the socket library.
import socket 
import sys
# creating a socket object 
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
print("Socket object binding is complete to the port ", PORT)
# putting the socket into listening mode mySocket.listen(5)
print("Socket is listening") 
c, addr = mySocket.accept()
data = c.recv(512)
if data:
  file = open("store.dat", "+w") 
  print("Connection from address : ", addr[0]) 
  file.write(addr[0]) 
  file.write(" : ")
  file.write(data.decode("utf-8"))
  file.close()
mySocket.close()
