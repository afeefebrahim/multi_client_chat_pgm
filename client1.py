import sys
import select
import socket
port = 4020
host = "127.0.0.1"
fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fd.connect((host,port))
inp = [fd,sys.stdin]
while True:
       inputready = select.select(inp,[],[])
       for s in inputready[0]:
           if s == fd:
                data = fd.recv(1024)
                if not data:
                    print "disconnect from chat server"
                    sys.exit()
                else: 
                    print "recived msg",data
           elif s == sys.stdin:
                msg = raw_input(">>")
                print msg
                fd.send(msg)
fd.close() 
