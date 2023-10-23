my_var = 10
print(my_var)
my_list = [1, 2, 3]
print(my_list)
print(*my_list) # 변수에 저장된 모든 값이 아니라, 리스트의 괄호까지 실행하려면 이렇게 별표 적는다


my_int = 10
# 부동소수점
my_float = 3.14
#복소수
my_complex = 3 + 4j
print(my_int)

my_character = 'A'
my_char = "0"
print(my_char)
my_string = 'Hello, World!'
str_name = "python"
print(my_string)
print(str_name)

my_bool = True
bFlag = False
print(my_bool)
print(bFlag)
my_list = [1, 2, 'three', True]
lsElement = [3.14, "b", "two", False]
print(my_list)
print(lsElement)

Nicolas = [1, 2, 3, ["진짜 수업 너무 별로다", "미정프는 제대로 된 게 없어", True]]
print(my_list)
print(*my_list)

# len
print(Nicolas.__len__())

print(my_list.__len__())
print(my_list[3]) # 인덱스로 접근 가능
list_el = my_list[2]

print(list_el) # three 출력

Animals = ["cat", "lion", "tiger", "duck", "rabbit"]
print(Animals)
# Animals[-1] = "pig" # 인덱스로 값 업데이트
print(Animals)

fusion = Animals[1] + Animals[0]
print(fusion) # 문자열끼리도 더할 수 있다. 그냥 붙어서 나온다

print(Animals[2:5]) # tiger duck rabbit
print(Animals[:3]) # cat lion tiger 
print(Animals[0:3]) # cat ling tiger 
print(Animals[4:]) # rabbit

# :3 이면 2까지 출력하고 3: 이면 3부터 출력한다. 

list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(list)
print(list[5][2]) # l 값이 존재하지 않는다
print(list[6][2:]) # 2 world
list.insert(2,4) # 2번째는 곧 8을 밀어내고 4를 두 번째에 삽입한다는 것을 말한다
print(list)
print(list.index(4))
list.append(22)
print(list) # * 문제 나오겠네

my_list = [10, 3, 8, 9, 42, 8, "Hello"]
print(my_list.count(5)) # 5가 있는 개수 출력, 지금 위의 리스트엔 5가 없다 그러므로 0

# print(my_list)
# print(my_list.pop()) # 아무 값도 쓰지 않으면 마지막 요소를 출력하고 삭제한다. 다시 프린트하면 없다
# print(*my_list)

player = [1, 2, 3, 4, 5]

print(player)
player.sort() # 오름차순으로 정렬
print(*player)

# player.reverse()
# print(*player) # 역순으로 정렬

versus = [6, 7, 8, 9]
print(player, versus)
player.extend(versus) # 리스트 결합
print(*player) # 1 2 3 4 5 6 7 8 9

versus.clear() # 리스트 내 모든 값 삭제
print(versus) # [] 출력

exam = [1, 2, 3]
print(exam)
exam.remove(2) # 인덱스처럼 순서 아닌 특정 값 삭제
print(*exam) # 1 3 출력

so = [11,22, 33, 44]
print(so)
del so[2] # 특정 인덱스 값만 삭제
print(*so)  

""" my_tuple = (1, 10, 'one', True)
tpItme = (3.14, "b", 'two', False)
my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(*my_tup)
print(my_tup.__len__())

my_tup = (5, 10, 11, 7, "WW", "MM")
print(my_tup)
print(my_tup[2])
print(*my_tup)

print(my_tup[2] + my_tup[0])
print(*my_tup)

n_add = my_tup[1] + my_tup[3]
print(n_add)

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:])

my_tup = (14, 2, 26, 1, "py", "w", ("AA", 8, 7, 3))
print(my_tup)
print(my_tup[6][0])

my_tup = (4, 2, 5, 1, "d", "a")
print(my_tup.index("d", 3, 5))
 """


person = {'age': '24', 'name': 'kim'}
print(person)

print(person["age"]) # 24 출력

my_str = person.get("name")
print(my_str) # 왜 굳이 이렇게 해야 되지

print(person.pop("age"))
print(person)

idx = ("a", "b", "c")
dicts = dict.fromkeys(idx, "0") # 각 값에 키값을 매겨주는 것
print(dicts) # a : 0, b:0 c:0 이런 식으로 나온다

cop = person.copy()
print(person)
print(cop)

my_dict = {'key1':'value1', 'key2' : 'value2'}
dicdata = {"name" : "python", "number" : 323265}
my_dict["key3"] = "value3" # 딕셔너리에 추가하는 방법
print(my_dict)

play = {'1' : 'dd', '2' : 'df'}
play.setdefault('3') # 값은 아니고 키만 넣어줌 '3' : None
print(play)

my_dict.update({"key1" : "v4"}) # 업데이트
print(my_dict)

del my_dict["key2"]
print(my_dict)

print("age" in person)
print("name" in person) # 있는지 없는지 확인, age는 없으므로 False, name은 True


just = {'nike' : 'shoes', 'adidas' : 'shirts'}
reabon = set(just.values()) # 그냥 just를 reabon으로 바꿔주는 것 value면 값이 나오고, key면 키만 나온다

print(reabon) # shirts, shoes

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.clear()
print(my_dict)  # 삭제