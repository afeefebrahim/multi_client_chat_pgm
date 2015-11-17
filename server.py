import socket
import select
import sys
size = 1024
port = 4020
host = "127.0.0.1"
fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
fd.bind((host,port))
fd.listen(5)
sock_list =[fd,sys.stdin]
while True:
       input_ready = select.select(sock_list,[],[])
       for s in input_ready[0]:
           if s == fd:
              client,addr = fd.accept()
              sock_list.append(client)
           
           elif s == sys.stdin:
              msg = raw_input(">>")
              for sock in sock_list:
                    if sock != fd and sock != sys.stdin:
                       sock.send(msg)
           
           else:
             
              data = s.recv(size)
              if not data :
                 print "disconnected from client"
                 sys.exit()
              else:
                 print data
    
              for sock in sock_list:
                      if sock != s and sock != fd and sock != sys.stdin: 
                            sock.send(data)
s.close() 
     
