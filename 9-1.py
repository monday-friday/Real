# 암호 처리
""" 
import getpass

pw = input("Pass :")
pw = getpass.getpass("Pass : ")

print(pw)

# 해시알고리즘
import hashlib

hl = hashlib.sha256()
target = "hello" """
# target = "hl"
# target = "world"
# target = "python"
# target ="mdeda"
# target ="intern"
# target ="12321"

""" 
hl.update(target.encode("utf-8"))
print(hl.hexdigest())
# print(hl.digest()) """

# keccak256

import Crypto.Hash.keccak as kak


# target = "hello"
# target = "hl"
# target = "world"
# target = "python"
# target ="mdeda"
# target ="intern"
# target ="12321"

target = "Intern"

kksh = kak.new(digest_bits =256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())

# 입력키 변환
""" 
import getpass
import hashlib

pw = input("Pass :")
pw = getpass.getpass("Pass : ")

hl = hashlib.sha256()

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
print(hl.digest())

import hashlib
import os
def pwInsert() :
    if os.path.exists('pw.txt') :
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else :
        return True
    
if pwInsert() :
    pw = input("new pass :") 
    with open('pw.txt', 'w') as fp:
	    hs = hashlib.sha256()
	    hs.update(pw.encode("utf-8"))
		fp.write(hs.hexdigest())
    
else : print("not allow password")   """  


# 시스템 정보

import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)


# 웹페이지 읽기

""" import urllib.request as ur

url = 'https://www.google.com'
res = ur.urlopen(url)
# res = urllib.request.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)

# print(web.decode('utf-8'))
print(web)

# 웹정보 읽기 2

import http.client as hc

url = "www.google.com"
# url = "https://www.daum.net"
# url = "https://www.google.com"
conn = hc.HTTPSconnection(url)
conn.request("GET", "/")


r = conn.getresponse()


with open("ulcl.html", "wb") as fp :
    fp.write(r.read())
    
conn.close()
print(r)    

import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)

print(web)
 """

# 멀티스레드
""" import time

import threading

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")

end = time.time()

print("singe end", end - start)


thread1 = threading.Thread(target=counter, args=("1num",))
thread2 = threading.Thread(target=counter, args=("2num", ))
thread3 = threading.Thread(target=counter, args=("3num", ))

start = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end")

# 멀티프로세싱

import multiprocessing as mp

def counter(str_name) :
    for i in range(50000) :
        print(f"countdown{i}, name : {str_name}\n")



process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))

start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc-end", end-start)
 """

# main 실행

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    #run()
    main()








