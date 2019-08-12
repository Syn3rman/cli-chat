import socket 
import select
import threading

def sendMessage():
  while True:
    message = input("{}>>".format(s.getsockname())) 
    s.send(message.encode('utf-8'))

def recvMessage():
  while True:
    data = s.recv(1024).decode('utf-8')
    if data:
      print("\n{}>>{}".format(s.getsockname(),data))

PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input("Enter the address of the server: ")
s.connect((HOST, PORT))
print("\nConnected to {}".format(s.getsockname()))
sendt = threading.Thread(target=sendMessage)
recvt = threading.Thread(target=recvMessage)
sendt.start()
recvt.start()