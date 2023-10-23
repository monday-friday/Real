""" x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)
print(x is z)
print(x is not z)
print(y is not z) # True

# 같은 값을 가지더라도 x와 y는 서로 다른 객체

a = 5
b = 7     
print(a is b) # false
print(a is not b) # true      
      
# 3 == 3.0
# 3 is 3.0      

a = 3
b = 3.0

print(a==b) # true 값은 똑같다.
print(a is b) # false, 그러나 객체는 다르다 is는 값이 같아도 안 된다.
print(a is not b) # true

a = [3, 5, 1]
b = a

a[0] = 2
print(a[0])
print(a is b)
print(b)

a[1] = 3
print(b)

# 연산자 우선순위, 사칙연산이랑 비슷함. 다만 괄호와 제곱이 제일 먼저라는 것만 기억
# 거듭제곱은 오른쪽에서 왼쪽으로 연산을 수행한다. 
x = 2 ** 3 ** 2 # 3 **2 가 계산되어서 9가 되고 2 ** 9가 된다. 
# 일반적인 연산말고 하나의 식씩 따로 계산한다고 생각하자
print(x)

a = 2 + 3 * 4
print(a)
a = 10 / 5 / 2
print(a)
a = 2 ** 3 ** 2
print(a)
a = 2 ** (3 ** 2)
print(a)
a = 10 % 3 % 2 
print(a) # 1 

a = 1 + 2 > 3 and 4 - 1 < 2
print(a)
a = not False and True
print(a)
a = not True or False and True
print(a) # not이 and or보다 우선순위가 높다. 이것만 봐서 False

a = 1 & 2 | 3 ^ 4
print(a)
a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(a)
a = 2 * -3 // 2 # //가 음수 연산자보다 우선순위가 높다
print(a) 
a = 1 == 2 != 3  # 왼쪽부터 하기 때문에 이미 판가름이 난 것이다 False
print(a)
 """
""" x = 0
if x > 0 :
    print("x is positive")
elif x < 0 :
    print("x is negative")
else :
    print("x is zero")

# if 짝수, 홀수

num = 23
if num % 2 == 0 :
    print("짝수")
else :
    print("홀수")

a = 1
b = 2
x = 3

# if 두 수 비교

if a == b :
    print("a is b")
else :
    print("a is not b")
   
# 문자가 a or b인지 비교   

char = "a"
if char == "a" or char == "b" :
    print("a 또는 b")
elif char != "a" or char == "b" :
    print("a 또는 b가 아닙니다")

if x == b :
    print(" x is b")
elif x == a :
    print("x is a")
else :
    print("둘 다 아님")

# for 변수 in 범위 :
# 실행할 코드

#for문 예시
fruits = ["apple", "banana", "cherry"]

for fruit in fruits :
    print(fruit)
 
 """
# 이중 for문 예시

# 0~9까지 출력
""" my_list = [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9] ]

for row in my_list :
    for num in row :
        print(num) 
# 여기서 row는 리스트 안의 리스트

for i in range(10) : 
    print(i)

# 문자열을 한 글자씩 출력
my_list = [["미", "디", "어"], ["정", "보", "프"], ["로", "그", "래"]]

for str in my_list :
    for me in str :
        print(me)

# 여기도 마찬가지로 str이 리스트 안의 리스트

for char in "python" :
    print(char)
# 명심하자 for반복문은 하나씩 실행한다. 문자열 역시 하나씩 출력된다

# 리스트 요소 반대로 출력(reversed 이용)

sports = ["baksetball", "soccer", "baseball"]

for sport in reversed(sports) :
    print(sport) 
    
# 리스트 요소 반대로 출력 (sorted 이용)
    
fruits = ["apple", "banana", "melon", "orange"]
    
for fruit in sorted(fruits, reverse = True) :
    print(fruit)    

# sorted는 본래 오름차순이다 reverse = True가 있어야 한다    

# 구구단 출력 (이중 for문 이용)

for i in range(1, 10) :
    for j in range(1, 10) :
        print(i, "x", j, "=", i*j)
# i 역시 1~10, j 역시 1 ~10이 있는 것이다     

# for ~ else 문

rang = [5, 7, 3, 1, 6]

for i in rang :
    print("element : ", i)
else : 
    print("end process")
    
        
# for 반복문 제어

for i in range(10) :
    if i == 9 :
        print("break", i)
        break
    elif i == 0 :
        print("continue", i)
        continue
    else :
        print("pass", i)
        pass
    print(i) 
    
   
# while 문

i = 0

while i <= 5 :
    print(i)
    i += 2


# 0부터 9까지 출력

i = 0

while i <= 9 :
    print(i)
    i += 1
 """
# 문자열을 한 글자씩 출력

""" str = ["p", "y","t", "h", "o", "n"]
i =0

while i <=5 :
    print(str[i])
    i += 1
else : 
    print("Nothing")
    
str_word = "python"
i = 0

while i < len(str_word) :
    print(str_word[i])
    i += 1
  
    
# 1부터 10까지의 총합 출력

sum = 0
i = 1

while i <= 10 :
    sum += i
    i += 1 """
    
print(sum)
    
# 1에서 100까지의 짝수, 홀수 출력하기
i = 1

while i <= 100 :
    if i % 2 == 0 :
        print("짝수", i)
    elif i % 2 == 1 :
        print("홀수", i)
    i = i+ 1 

# 아이, 들여쓰기 잘 보자. elif에 i=i+1이 속하면 홀수일 때만 작동하고 그렇게 되면 if문만 실행한다

# 1에서 100까지의 7의 배수만 출력하기

i = 1

while i <= 100 :
    if i % 7 == 0 :
        print(i)
    i = i + 1


