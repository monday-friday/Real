""" my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print(my_set)
print(setItem)


my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
print(*my_set)

my_set = ([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")
print(set_tmp) # Hello가 각각 따로 출력

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
# print(my_set | set_item)
print(my_set.union(set_item)) # 두 집합을 더해준다

print(my_set | set_item)
# print(my_set - set_item) 빼는 것

print(my_set.difference(set_item)) # 1, 3, 5 두 집합에서 겹치지 않는 요소

# print(my_set & set_item)

print(my_set.intersection(set_item)) # 겹치는 요소만 출력

print(my_set) # 1 3 5 7 8 h
my_set.add(9)
print(my_set) # 1 3 5 7 8 9 h
my_set.update([5, 9, 7, 4])
print(my_set) # 1 3 4 5 7 8 9 h 업데이트는 더해주는 것이다

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
# my_set.clear()
my_set.remove(5)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set) # 공통된 요소 삭제

my_int = 10
my_str = str(my_int)
print(my_int)
print(my_str)

my_int = 10
print(my_int)
print(my_int + 10)

my_int = 10
print(my_int)

print(my_int + 10)
my_str = str(my_int)
print(my_str)

my_int = 10
print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)

print(my_str + "hello")

# my_str = '10'
# my_int = int(my_str)
# print(my_str)
# print(my_int)

my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)
 """
# my_int2 = int("ten")
# print(my_int2)

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b) # 몫구하기
print(a ** b) # 거듭제곱

a = 10
b = 4
print(a // b) # 값은 2


print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b) 

a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a)

a /= 2
print(a)

a**=3
print(a) # 8.0

# 쉽게 생각해서 더하고 저장, 빼고 저장, 곱하고 저장 이렇게 되는 것이다 return처럼 a에 값이 저장된다

a = 10
b = 4

print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   # 파이썬은 왼쪽에서 오른쪽으로 읽는다. a가 b보다 작거나 같다라는 의미!
print(a == b)  
print(a != b) # 같지 않다  

a = 1
b = 0

# 전기가 통할 때가 1 안통할 때가 0이다. 즉 1이 True, 0이 False
print(a and b) # 0 
print(a or b) # 1
print(not a) # False not A는 곧 0이라는 의미
print(not b) # True

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y)

print("==============")

print(x & y) # false
print(x | y) # true
print(x ^ y) # true XOR 연산자는 입력값이 같지 않으면 1을 출력한다
print(~x) # -2
print(x << 2) # 4


a = 10
b = 3

print(a & b) # 2
print(a | b) # 11
print(a ^ b) # 9
print(~a) # -11
print(a << 2) # 40

my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list) # 요소가 리스트에 있는지 확인

print(2 in my_list)
print( 2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_dic) 