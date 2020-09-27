import socket

def serverside():
    host = socket.gethostname()
    print(host)
    port = 5000 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    con, addr = s.accept()
    print("Waiting for connection")
    print("Connection from : "+ str(addr))
    while True:
        data = con.recv(1024).decode()
        if not data:
            break
        print("from Connected User: " + str(data))
        data = input("Provide Data ->")
        con.send(data.encode())
    con.close()
if __name__ == '__main__':
    serverside()    
