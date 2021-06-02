import socket
mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()#encode prepares the data to go across the internet
mysocket.send(cmd)

while True:
    data=mysocket.recv(512)#512 characters each time
    if (len(data)<1):
        break
    print(data.decode())
mysocket.close()