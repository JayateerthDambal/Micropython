import socket

def instance():
    host = '192.168.43.13'
    print(host)
    port = 2000
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ms.bind((host, port))
    ms.listen(5)
    con, addr = ms.accept()
    print("Waiting for Connection")
    print("Connected to -> "+ str(addr))
    while True:
        data = con.recv(1024).decode()
        if not data:
            break
        print("from node:GPIO status"+ str(data))
        data = input("Give reponse-> ")
        con.send(data.encode())
    con.close()

if __name__ == '__main__':
    instance()        
