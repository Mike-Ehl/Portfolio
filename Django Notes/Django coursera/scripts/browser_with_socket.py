#%%
import socket

#This is the simplest way of surfing the internet uising python
#To do so, we'll use a socket, creating a socket object and then
#using the connect method, we'll connect to a server and, using the recv()
#method, we can receive the data since the connection is already stablished

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(), end = "")

mysock.close()
# %%
