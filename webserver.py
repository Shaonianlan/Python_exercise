import socket
import time

s = socket.socket()
port = 5005
s.connect(('localhost',port))
s.send('woshi sazi'.encode())
time.sleep(100)