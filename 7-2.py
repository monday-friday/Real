""" import socket
from select import select
import time

HOST = "127.0.0.1"
#HOST = "localhost"
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

#1.소켓 생성.
srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.주소 정보 할당
srvSock.bind(ADDR) 
print('bind')

#3.수신 대기 상태
srvSock.listen(100) 
print('listen')

#4.연결수락
cltSocket, addr_info = srvSock.accept() 
print('accept')

time.sleep(10)

#연결 종료
cltSocket.close() 

#소켓 종료
srvSock.close()

print('close')


import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)


#1 서버에 접속하기 위한 소켓을 생성한다.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 서버에 접속을 시도한다.
clientSocket.connect(ADDR)
print('connect is success')


import socket
from select import select
import time

HOST = "127.0.0.1"
#HOST = "localhost"
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvSock.bind(('', PORT))
srvSock.listen()

cltSocket, addr = srvSock.accept()

while True:
    response = cltSocket.recv(1024)
    print ('client : ', response.decode('utf-8'))

    message = input('server : ')
    cltSocket.send(message.encode('utf-8'))

cltSocket.close()



import socket
import sys

import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))

clientSocket.close()



import socket

HOST = "127.0.0.1"
PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("msg: ", data)

    rsp = data.decode("utf-8").upper()
    sock.sendto(rsp.encode("utf-8"), addr)

sock.close()



import socket

HOST = "127.0.0.1"
PORT = 1234

ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("msg : ")

    sock.sendto(msg.encode('utf-8'), ADDR)
    rsp, srv = sock.recvfrom(1024)
    print("msg : ", rsp)

sock.close()
 """


class Person :
	name = "python"
	age = 23
	number = "01012345678"

p = Person()
p.name

print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)

# 메서드
""" class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce()) """

""" class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number

p = Person("hello", 24, "01012030232")
p1 = Person("Yes", 23, "01210")

print(p.name)
print(p1.name)

print(p.number)
print(p1.number)


class Person :
	count = 0
	
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
    
def getCount(cls) : 
	return cls.count
  
p = Person("Got", 11, "dfd") 
print(p.name) 
print(p.count)  

p1 = Person("wit", 88, "None")
print(p1.age)
print(p1.count)

print(p.getCount())
print(p1.getCount()) """




