'''

#exception file read

import os 

fp = "temp.txt"

if os.path.exists(fp):
    f=open(fp, "r")
    for line in f :
        print(line)
    else:
        f = open(fp, "w")
        for i in range(100) :
            f.write(str(i)+"\n")
        #print("error")
        
    f.close()
    
    #파일 삭제
    
    import os
    fp= "new.txt"

f = open(fp, "w")
f.close()

os.remove(fp)
print("complete")

#dir출력

import os

def dir_print(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"

f=open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("------------------------------\n\n")
dir_print("./")


#파일명 변경

import os
fp = "new.txt"

f=open(fp,"w")
f.close()

os.rename(fp,"new1.txt")
print("comlate")

#재변경 예외처리

import os 

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close() 

if os.path.exlsts(tp) :
    print("exist, smae name file")
    os.remove(tp) 
else :
    os.rename(fp, "new1.txt")
    print("complate")
    

#파일명 변경 확인

import os
def dir_print(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

dir_print("./")
print("=============================")     

if os.path.exists(tp):
    os.remove(tp)
    dir_print("./")
    print("exist, same name file")
else:
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete")
    
    

#with

#f = open("temp.txt", "r")
with open("temp.txt", "r") as f:
    print(f.read())
    
    #for i in range(110):
    #    res = f.readline()
    #    print(res)
    
'''
'''
#속성 출력

class Person :
    name = "python"
    age = 23
    number ="01012345678"
    
    def getIntroduce(self):
        return f"My name is {self.name}"
    
p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)
'''

#클래스 초기화
'''
class Person :
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        
p = Person("helllo", 24, "01087654321")
p1 = Person("he", 21, "0108")
p2 = Person("hee", 24, "028764321")

print(p.name)
print(p1.name)
print(p2.name)

'''
#클래스
""" 
class Person :
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        Person.count += 1
        
p = Person("helllo", 24, "01087654321")
print(p.name)
print(p.getCount())
p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.getCount())
p2 = Person("hee", 24, "028764321")
print(p2.name)
print(p2.getCount())
 """
