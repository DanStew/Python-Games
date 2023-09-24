import socket

"""
This file is going to create a class that allows a client to connect to a server
This class can be reused, as well in other projects where networking is needed
"""

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.233.207.59"
        self.port = 5555
        self.address = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    
    def connect(self):
        try:  
            #When you connect, you should send back some id or something back to show that that device has connected
            #This code below implements that
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try : 
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
print(n.send("hello"))
        