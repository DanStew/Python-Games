import socket
from _thread import *
import sys

"""
Running the server and client script
The server script must always be running
Whenever doing this, you must first setup the server script
You can then add as many client scripts afterwards to be able to connect to the server
You can run multiple client scripts on the same machine, as well as also run the server
"""


#The ip address for this is found by going to the command prompt and typing ipconfig
#Then, use the ipv4 address of the bottom set that comes up for the address
server = "10.233.207.59"

port = 5555 #Need to use a port that you know will be left open

#Setting up the socket to be used
#Sockets basically use a port on your computer to look for certain connections
#AF_INET allows you to connect to an IPv4 network (IP Addresses)
#SOCK_STREAM defines how the server string (above) comes in
#This is usually the socket code needed for all types of these applications
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the server and port to the socket
#Try and Except needed as you don't know whether it will actually work straight away
try : 
    socket.bind((server,port))
except socket.error as e:
    str(e)

#Opens up the port to listen for connections
#Allows clients to be able to connect to the port
#The argument is the amount of people able to connect to the server
socket.listen(2)
print("Waiting for a connection, Server Started")

#Defining the threading function
#A thread is just another process running in the background
#This means that this code can be run, when startnewthread is called
#This code can continue running without needing to be completed, and the code will still continue to move on
#Means you don't have to wait for the function to run
def threaded_client(connection):
    reply = ""
    while True:
        try : 
            #Trying to collect data from the connection
            #2048 is defining the amount of bits allowed (or something to do with bits)
            #The larger the size is, the longer it takes to recieve the information
            data = connection.recv(2048)
            #Reading the information from the data
            reply = data.decode("utf-8")

            if not data:
                #Disconnecting from the client, when connection fails
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
            
            #Sending the information to the server
            #You have to encode the data back into bytes, which is what this does
            connection.sendall(str.encode(reply))
        except :
            break

#While loop to continuously look for connections
while True : 
    #Connection is an object representing what's connected
    #Address is the IP address of the computer connected
    connection, address = socket.accept()
    print("Connected to: ", address)
    #This function is imported from _thread
    start_new_thread(threaded_client, (connection,))
