# 미니프로젝트
# 삼각형 추력

# 직각삼각형 출력
for i in range(1, 6) :
    print("*" * i)

# 역직각삼각형
for i in range(5, 0, -1) :
    print("*" * i) # -1 부터는 거꾸로 5부터 실행한다는 의미
    
# 이등변삼각형
for i in range(1, 6) :
    spaces = " " * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars)    
    
print("=======================")    

# n = 5 # 삼각형의 높이를 설정
for i in range(6, 0 , -1) :
    spaces = " " * (6 - i)
    sars = "*" * (2 * i -1)
    print(spaces + stars)
 
# 5 x 5 출력

# 출력예시 - 정상출력
num = 0
line = []
for i in range(5):
    for j in range(5) :
        num += 1
        line.append(num)
    print(line)
    line = []
    
# 세로로 출력

line = []
for i in range(1, 6) :
    for j in range(1, 6) :
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = [] 

# 출력 예시 - 역순출

num = 26
for i in range(1, 6) :
    for j in range(1, 6) :
        print(num)
        num -= 1
        line.append(num)
    print(line)
    line  = []   

# 가위바위보 게임
# 가위 = 1, 바위 = 2, 보 = 3
# 함수 1 : random 모듈 choice를 이용, 상대의 결과값 추출
# 함수 2 : 입력값과 추출값을 비교해 승패 결정

import random

def get_computer_choice() :
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice) :
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice ** pcnum : 
        print("무승부")
        return
    elif (
        (user_choice ** '1' and pcnum ** '3') or
        (user_choice ** '2' and pcnum ** '1') or
        (user_choice ** '3' and pcnum ** '2') 
    ) :
        print("승")
        return
    else :
        print("패")
        return
    
print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1 ~ 3 숫자를 입력하세요!")
chnum = input()
#pcnum = get_computer_choice()

determine_winner(chnum) 

# 6-1 파일처리

# 파일 생성 code 파일, 원래 설정되어 있던 경로에 파일 생성됨
f = open("real.txt", "w")
f.close()

# 파일 쓰기

file = open("real.txt", "w")

file.write("hello\n") # 역슬러시n을 쓰면 한 줄이 생긴다. 제어 문자라 칭함
file.write("world")

file.close()

# 파일 쓰기

file = open("real.txt", "w")

for i in range(100) :
    file.write(f"{i}\n")

file.close()     


f = open("c:\\User\\Catholic\\temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")

f.close()

# 추가 쓰기
file = open("c:\\User\\Catholic\\real.txt", "a")

file.write("hello\n")
file.write("world")

file.close()
 

# 파일 읽기

file = open("c:/User/Catholic/real.txt", "r")
res = file.read()
print(res)

file.close()


# 다른 경로 파일 읽기

file = open("c:/User/Catholic/real.txt", "w")
res = file.read()
print(res)
file.close()

# readline

file.readline()
file = open("real.txt", "r")
file = open("real.txt", "r")

res = file.readline()
print(res)

for i in range(110) :
    res = file.readline()
    print(res)

file.close()


# readline 전체읽기

f = open("real.txt", "r")
res = f.readline()
print(res)

f.close()

# readline 읽기

f = open("real.txt", "r")
line = f.readline()
for l in line :
    print(l)

f.close()

# 파일 객체로 읽기
f = open("real.txt", "r")
for line in f :
    print(line)

f.close()











