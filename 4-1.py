""" #input

num = input("숫자를 입력하세요!!")
print("number", num)

# 데이터 타입을 알려준다

a = "abd"
print(type(a)) 

a = 12.94
print(type(a))

a = [3,2,1]
print(type(a))  """
""" 
a = 65

# print(int(a))
# print(str(a))
print(hex(a))
print(oct(a))
print(chr(a))
print(ord("A"))

print(pow(2, 2))
print(pow(2, 3))
print(3 ** 5)

# print(divmod(10, 3))
print(round(3, 141))
 """
""" a = (3, 5, 7)

b = list(a)
c = tuple(b)

print(b)
print(c) """
# 그냥 리스트, 튜플 형태로 나온다. 괄호만 주의하자

# range

""" for i in range(2, 7) : 
    print(i)

for i in range(6) :
    print(i)

# 이렇게 7 혹은 6까지라면 출력되는건 6까지, 그리고 5까지다

for i in range(1, 28, 3) : 
    print(i)
# 맨 뒤에 있는 3씩 더한다. 1부터 3씩 더해서 28 전까지 나온다
    
 # max, min, sum   
    
a = [3, 4, 6, 9]

print(max(a))
print(min(a))
print(sum(a)) # 22 총합이다

# abs 음수를 양수로, 바꿔준다

print(abs(-3)) 
print(abs(3.0))
print(abs(-3.0))

#sorted
a = [5,7, 3, 4, 6,]

print(sorted(a))
print(sorted(a, reverse = True))


# enumerate

a = [5, 3, 14, False, 9, "try"]
print(enumerate (a))
print(*enumerate(a)) """

# 인덱스와 함께 값을 반환한다. 즉 0번째는 5이므로 (0,5) 이런 식으로

# zip

""" a = [1, 2, 3]
b = [4, 5, 6]
print(*zip(a, b)) # (1, 4) (2, 5) (3, 6) 이런 식으로 두 개 합쳐서 나온다


# any, all
a = [True, True, False]
print(any(a)) 
print(all(a))
# 둘 다 True인지 False인지 확인한다 any는 단어 그대로 or, all은 and연산

#format
a = 20
b = 23
print("a는 {}, b는 {}, {}".format(a,b, "python")) """
# 그냥 포맷하면 문자열만 나온다고 생각

#global~ callable

""" a = 3
print(globals()) 
print(locals()) 
 """
# print(dir(a))

# print(callable(a))

# lambda 함수
""" 
add = lambda a, b : a + b
print(add(2, 3))

sub = lambda a, b : a - b
print(sub(5, 2))

mul = lambda a, b : a * b
print(mul(2, 12))

div = lambda a, b : a / b
print(div(6,2))  """

# 사용자 정의 함수

""" def function(parameter) : 
    return result  """

""" def add_numbers(x,y) : 
    return x + y

result = add_numbers(4, 5)
print(result) """


# 매개변수, 인자

""" def greet(name) : 
    return name

result = greet("paul")
print("Hello, " + result + ". How are you?") """

""" def add(a, b) :
    print(a + b)

def sub(a, b) :
	print(a - b)

def mul() :
	print(2 * 4)

def div() :
	print(4 / 2)

add(3, 5)
sub(3, 5)
mul()
div()
 """

# 1. 입력받은 수가 짝수/홀수인지 판별하는 함수
""" def is_even(n) :
    if n % 2 == 0 :
        print("짝수")
    else : 
        print("홀수")
        
num = input("숫자를 입력하세요 : ") 
is_even(int(num))    
 """
# 2. 문자열을 입력받아 문자열 반대로 출력하는 함수


""" food = ["meat", "rice", "vegetables"]

for food in reversed(food) :
    print(food) 


def reverse_stirng(msg) :
    return msg[::-1] # 뒤에서부터 -1부터 끝까지

in_str = input("문자열 : ")
print(reverse_stirng(in_str)) """


# 3. 두 수를 입력 받아 사칙연산 결과 출력하는 함수

""" def add(a, b) :
    return int(a) + int(b)

def sub(a, b) :
    return int(a) - int(b)

def mul(a, b) : 
    return int(a) * int(b)

def div(a, b) :
    return int(a) / int(b)


a = input("a를 입력하세요")     
b = input("b를 입력하세요")

print("더하기: ", add(a, b))
    
print("빼기 :", sub(a, b))    """
    
""" print("곱하기 :", mul(a, b))  
    
print("나누기 :", div(a, b))      
     """
    
# 4. 5개의 숫자를 입력받아 총합을 출력하는 함수
""" def sum_num(num) :
    return sum(num)

nums = [] # 현재 비어있는 상태, None

for i in range(1, 6) :
    innum = int(input(f"{i} 번째 숫자 입력 : ")) 
    nums.append(innum) # 여기서 nums에 데이터 추가
    
print(sum_num(nums))    
     """
    
    