import socket
from machine import Pin
led = Pin(4, Pin.IN)
led.value(0)

def client():
    host = '192.168.43.201'
    port = 2000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    allow = True
    
    try:

        while allow:
            if led.value() == 0:
                msg = 'Led is OFF, Do You want to turn it On y/n??'
                s.send(msg.encode())
                data = s.recv(1024).decode()
                val = print("Admin responded->>" + str(data))
                if val == 'y':
                    print("Led turned On")
                    led.value(1)
                else:
                    led.value(0)

            else:
                msg = 'Led is ON, Do you want to turn it OFF y/n?'
                s.send(msg.encode())
                data = s.recv(1024).decode()
                value = print("Admin responded-->" + str(data))
                if value == 'y':
                    led.value(0)
                    print("Led turned Off")

                else:
                    led.value(1)
                    print("Led is ON")

        s.close()
    except KeyboardInterrupt:
        print("User Ended Program!!!!")
        allow = False


if __name__ == '__main__':
    client()
