# 파일 생성

import os

fp = "four.txt"
#file = "temp1.txt"

# file = open(fp, 'w')

if os.path.exists(fp) :
	f = open(fp, "w")
for line in f :
        print(line)
    # file = open("five.txt", "w")
else :
    f = open(fp, "w")
    for i in range(100) :
        f.write(str(i) + "w")
	# print("error")
    # file = open("six.txt", "w")

f.close()    
    
    
# 위는 정상적인 코드는 아니고, 그냥 예시

# 파일 삭제
""" os.remove(fp)
print("complete") """


""" def dir_print(p) :
    files = os.listdir(p)
    for f in files :
        print(f)

fp = "two.txt"
f = open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("=======================\n\n") 
dir_print("./") """
 

# 재변경 메모처리

import os
fp = "new.txt"
tp = "next.txt"

f = open(fp, "w")
f.close()

if os.path.exists(tp):
    print("exist, save name file")
else :
    os.rename(fp, "next.txt")
    print("complete")    

# 파일명 변경 확인

def dir_print(p) :
    files = os.listdir(p)
    for f in files :
        print(f)
 
 
fp = "new.txt"
tp = "next.txt"
        
f = open(fp, "w")
f.close()

dir_print("./")
print("=======================\n\n") 

fp = "new.txt"
tp = "next.txt"

if os.path.exists(tp):
    print("exist, save name file")
else :
    os.rename(fp, "next.txt")
    print("complete")    

# with

with open("aye.txt", "r") as f :
    print(f.read())

    for i in range(100) :
        res = f.readline()
        print(res)







 
 
 
 
 
 
 
 