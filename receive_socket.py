#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

import socket
import base64
import codecs
import time

size = 300

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('192.168.43.159', 8000))
#serv.bind(('0.0.0.0', 8000))
serv.listen(5)

print ("waiting for data tx")

#while True:
conn, addr = serv.accept()
data = conn.recv(size)
print ("data received")
conn.send(bytes("status: received\n", "utf8"))
with open("tmp.txt", "w") as fh:
    fh.write(str(codecs.decode(data, 'base64')))
done = True
time.sleep(0.1)
        
conn.close()
print ("client disconnected")

    
