import socket
import select

HOST = '0.0.0.0'
PORT = 1235

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST,PORT))
  s.listen()
  conn, addr = s.accept()
  s.setblocking(0)
  # list of clients that can take and send data to server
  inputs = [conn]
  outputs = []
  messages = []
  # select requires 3 arguments: list of the objects to be checked for incoming data to be read, the second contains objects that will receive outgoing data when there is room in their buffer, and the sockets that may have an error
  while True:
    (readables, writables, exceptions) = select.select(inputs, outputs, inputs)
    # Go through all the sockets that can send and recieve data
    # Recieve data from sockets sending them and broadcast data to all listening sockets
    for readable in readables:
      # print(readable, inputs)
      if readable is s:
        # Ready to accept new connections
        connection, clientAddress = s.accept()
        connection.setblocking(0)
        inputs.append(connection)
        print(inputs)
      else:
        data = readable.recv(1024).decode('utf=8')
        if data != "":
          print("Recieved {} from {}".format(data, readable.getpeername()))
          messages.append(data)
          if readable not in outputs:
            outputs.append(readable)
        else:
          # close connection
          if readable != conn:
            inputs.remove(readable)
          print(readable, inputs)
    for message in messages:
      try:
        # print(inputs)
        if inputs:
          s.send(message.encode('utf-8'))
      except:
        pass