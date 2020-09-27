import socket

def clientside():
   host = socket.gethostname()
   print(host)
   port = 5000
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((host, port))
   msg = input(" --> ")
   while msg.lower().strip() != 'bye':
      s.send(msg.encode())
      data = s.recv(1024).decode()
      print("Received from User-> " + str(data))
      msg = input(" --> ")
   s.close()

if __name__ == '__main__':
   clientside()

