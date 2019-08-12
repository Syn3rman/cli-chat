import socket
import select

HOST = '0.0.0.0'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST,PORT))
  s.listen()
  # list of clients that can take and send data to server
  connectionList = [s]
  # select requires 3 arguments: list of the objects to be checked for incoming data to be read, the second contains objects that will receive outgoing data when there is room in their buffer, and the sockets that may have an error
  while True:
    (readSocks, writeSocks, exceptions) = select.select(connectionList, connectionList, [])
    # Go through all the sockets that can send and recieve data
    # Recieve data from sockets sending them and broadcast data to all listening sockets
    for sock in readSocks:
      # print(sock, connectionList)
      if sock is s:
        # Ready to accept new connections
        connection, clientAddress = s.accept()
        connectionList.append(connection)
      else:
        # read data from emitting sockets
        try:
          data = sock.recv(1024).decode('utf=8')
          if data != "":
            print("Recieved {} from {}".format(data, sock.getpeername()))
            for wrSock in writeSocks:
              if wrSock.getpeername()!=sock.getpeername(): 
                wrSock.send(data.encode('utf-8'))
          else:
            connectionList.remove(sock)
        except:
            # close connection
          print("closing connection")  
          connectionList.remove(sock)