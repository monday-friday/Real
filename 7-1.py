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
 
# 위는 정상적인 코드는 아니고, 그냥 예시






 
 
 
 
 
 