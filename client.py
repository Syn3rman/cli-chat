import socket 
import select, json
import threading

def sendMessage():
  while True:
    message = input("{}>>".format(username)) 
    s.send(message.encode('utf-8'))

def recvMessage():
  while True:
    data = s.recv(1024).decode('utf-8')
    data = json.loads(data)
    if data:
      print("\n{}>>{}".format(list(data.values())[1], data['data']))

PORT = 1235

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input("Enter the address of the server: ")
username = input("Enter username: ")
s.connect((HOST, PORT))
s.send(username.encode('utf-8'))
print("Connected to {}".format(s.getsockname()))
sendt = threading.Thread(target=sendMessage)
recvt = threading.Thread(target=recvMessage)
sendt.start()
recvt.start()