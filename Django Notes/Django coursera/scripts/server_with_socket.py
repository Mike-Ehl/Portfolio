#%%
from http import server
from socket import *

def createserver():
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        serversocket.bind(('localhost', 8000))
        serversocket.listen(5)
        while(1):
            (cliensocket, address) = serversocket.accept()

            rd = cliensocket.recv(5000).decode()
            pieces = rd.split('\n')
            if len(pieces) > 0 : print(pieces[0])

            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type: text/html, charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            cliensocket.sendall(data.encode())
            cliensocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print('\n Shutting down \n')

    except Exception as exc :
        print('Error:\n')
        print(exc)

    serversocket.close()

print("Access http://localhost:8000")
createserver()

# %%
