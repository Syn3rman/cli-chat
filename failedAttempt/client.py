import socket 
import select
import threading

def sendMessage():
  while True:
    message = input("Enter message to be sent: ") 
    print("Sending message: {} ".format(message))
    s.send(message.encode('utf-8'))

def recvMessage():
  while True:
    data = s.recv(1024).decode('utf-8')
    if data:
      print("Recieved {} from {}".format(data, s.getsockname()))

PORT = 1235

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input("Enter the address of the server: ")
s.connect((HOST, PORT))
sendt = threading.Thread(target=sendMessage)
recvt = threading.Thread(target=recvMessage)
sendt.start()
recvt.start()
print("Connected to {}".format(s.getsockname()))