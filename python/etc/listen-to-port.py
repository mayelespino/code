#!/usr/bin/python
#http://docs.python.org/release/2.4.2/lib/socket-example.html
# Echo server program
import socket
import sys

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
#PORT=80
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error, msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except socket.error, msg:
            s.close()
            s = None
            continue
            break
if s is None:
    print 'could not open socket'
    sys.exit(1)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    myData = data
    print "data ",data
    if not data: break
    #if 'exit' in data: break
    conn.send(data)
conn.close()

