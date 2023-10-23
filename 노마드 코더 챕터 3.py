""" # 3 0 Methods
# 데이터 구조화에 대해 해볼 것이다
# 파이썬의 데이터 구조는 3가지

# 일주일의 요일을 목록으로 써봐라
mon = "mon"
tue = "tue"

# 이건 변수의 나열이지, list가 아니다. list는 variable 한 개 안에 있어야 한다

days_of_week = "mon, tue, wed, thu, fri"

# 이 방식의 문제점은 만약 수요일만 달라고 하면 어떻게 하지? list가 필요한 이유

days_of_week2 = ["mon", "tue", "wed", "thu", "Fri"]
Miami_Heat = ["buttler", "adebayo", "hiro", "robinson"]
# list는 대괄호를 쓰고 안에 데이터를 써준다
# list를 만든 이유는?
print(days_of_week2)
print(Miami_Heat)
# 별 차이 없나? method를 아직 배우지 않았기 때문

name = "kim"

# 닷, .을 찍으면 뒤에 뭐가 많다. 
# "kim"이라는 건 단순 텍스트가 아니야. 내부에 다양한 function을 가지고 있다.
# 점 뒤에 보이는 모든 function은 name이라는 변수에 결합되어 있다
# print는 결합되지 않아서 아무데서나 아무렇게 사용할 수 있다. 근데 name은 string이고
# string 안엔 수많은 function 정확히는 method가 있다.
# method는 데이터 뒤에 결합된/연결된 function

print(name.upper())
# upper method가 name의 데이터를 가져와서 대문자로 바꿔준다
print(name.capitalize())
# capitalize가 첫 문자를 대문자로 바꾼다
# 즉 data 안에 결합된 수많은 펑션, method가 있다
print(name.startswith("n"))
# 데이터가 n으로 시작되는게 맞는지 확인
print(name.replace("m", "jeol"))
# 문자를 대체하는 replace
print(name.endswith("m"))
# m으로 데이터가 끝나는지 확인

print("kim".endswith("m"))
# name은 그냥 변수다. 이렇게 해도 무방하다


# 3 1 Lists
# 함수가 데이터와 결합되어 있다면 메소드, 복습!

size = ["L", "S", "M", "L", "L", "S"]

print(days_of_week2.count("wed"))
print(size.count("L"))

# count로 수요일이 몇 개나 있는 지 셀 수 있다
# 리스트의 장점 하나, 데이터에 적용 가능한 멋진 메소드를 쓸 수 있다

# days_of_week2.clear()

print(days_of_week2)

# clear은 리스트의 아이템을 삭제한다
# clear 메소드는 day 리스트를 변경시킨다고 볼 수 있다

days_of_week2.reverse()
print(days_of_week2)

# reverse는 리스트의 데이터를 거꾸로 실행한다

days_of_week2.append("sat")
days_of_week2.append("sun")
print(days_of_week2)

# append는 리스트 안에 있고, 이걸로 리스트 안에 데이터를 추가할 수 있다

days_of_week2.reverse()
days_of_week2.remove("Fri")
print(days_of_week2)

# remove는 데이터를 제거한다

# 만약 리스트의 특정 데이터를 갖고 싶다고 한다면?
# 대괄호를 열고 리스트에서 너가 접근하고 싶은 아이템의 인덱스를 넣어주면 된다. 0부터 세자

print(days_of_week2[2])
days_of_week2.append("Hot") 
print(days_of_week2) # 결과['sun', 'sat', 'mon', 'tue', 'wed', 'thu', 'Hot']

# 리스트가 꼭 문자열일 필요는 없다. 숫자, 불데이터도 가능하다. 리스트 안에 리스트도 가능하다
# example = [True, False, True, 12, 28, [1, 2, 3], ["Fun", "Sad"]]

# 3 2 Tuples
# tuple 만드는 방법. 대괄호 대신에 소괄호를 쓰면 된다 () 이거
days = ("mon", "tue", "wed")
# 튜플과 리스트의 차이점은 튜플은 불가변성을 지닌다. 내용을 바꿀 수 없다
days = ["mon", "sat", "Fri"]
print(days[0])
# 리스트에서 했던 것처럼 인덱스로 아이템에 접근할 수 있다. 대괄호로 아이템에 접근한다
print(days[-3])
# 아이템은 뒤에서부터 앞으로도 접근할 수 있다. 뒤에서 -1부터도 가능하다. 튜플, 리스트 모두 마찬가지
# 리스트로만 데이터를 변경할 수 있음을 명심해라 """

# 3 3 Dicts
# dictionary에 대해 알아보자
# 딕셔너리엔 중괄호를 써준다
""" player = {'name' : ['kim', "h"], 'age' : 24, 'alive' : True, 
          'fav_food' : ["chicken", "soup"]
          }

print(player.get('fav_food'))
print(player.get('name'))
# 딕셔너리에도 메소드가 있다. 
# get은 특정 데이터를 가져온다
# 딕셔너리에는 키와 값으로 이루어져 있다. 왼쪽이 키, 오른쪽이 값
# 딕셔너리는 많은 속성을 가진 데이터를 만들 때 쓰인다

print(player['fav_food'])
print(player['age'])
# get을 쓰지 않고 위처럼 작성해도 데이터를 불러올 수 있다
# 인덱스 접근하는 것처럼 생각해보자
# 딕셔너리 또한 아이템 변경이 가능하다

print(player)
player.pop('age')
print(player)

# pop은 특정 데이터를 없앤다

print(player)
player['weight'] = 65
player['height'] = 173
print(player)

# 데이터를 추가하는 방법은 딕셔너리 [키] = 값 이다
# fav_food에 새로운 음식을 추가하는 방법
# fav_food는 대괄호로 되어 있다. 즉 리스트라는 것 리스트에 메소드를 쓸 수 있다

player['fav_food'].append("noodle")
player['name'].append("chi")
# 딕셔너리 안의 리스트이므로 이렇게 써줘야 한다
# 딕셔너리[키] .어펜드 (추가할 아이템) 으로 추가해준다

print(player.get('fav_food'))
print(player['fav_food'])
print(player['alive']) """
# 이 두 개는 같은 작용이다
# 참고로 '나 "나 둘 다 똑같다. 뭘 써도 상관없다. 헷갈리지 말자

# 3 4 Recap

""" "home".upper()
print("home".upper())

# 메소드를 찾고 사용할 땐, 데이터 이름 뒤에 온점을 찍은 후 메소드를 적어준다
# 메소드는 함수다. 소괄호를 쓰면 사용한다는 의미

# 어떠한 데이터든 값들의 목록을 만들게 해준다. 그러나 리스트의 파워는 메소드에 있다
numbers = [1, 2, 3, 4, 5, True, "Dongwonchamchi"]
numbers.append("sajo")
print(numbers)
# 또한 아주 편한 방법으로 이러한 값들을 변경할 수 있도록 해준다
numbers.pop(2) # 숫자 데이터를 지울 경우 인덱스로 지워야 한다. 여기서 2는 세 번째 숫자인 3을 지운다
print(numbers)
# 인덱스로 리스트의 특정 아이템에 접근할 수 있다
print(numbers[5])
print(numbers[-2])
print(numbers[-1]) # 이건 sajo가 나온다
# True가 나올까? 그렇지 않다 중간에 사조를 추가했으니까, 동원참치가 나온다

number = [1, 2, 3, [5,6], False]
# 이렇게 리스트 안에 리스트가 또 존재할 수 있다

# 튜플은 소괄호로 생성한다
newjeans = ("hypeboy", "attention", "omg", "ditto", "supershy", "eta")
print(newjeans[-3])
# 리스트와 똑같은 방법으로 접근할 수 있다

# 딕셔너리는 키와 값으로 이루어져 있다
player = {'dd' : 'man', 
          'name' : 'God',
          'alive' : True,
          'fav_food' : ('Haejang', 'yookhoi'),
          'friend' : {'name': 'lena', 'age' : [22]}}

# 딕셔너리 안에는 리스트와 튜플을 넣을 수도 있고 또 다른 딕셔너리를 넣을 수도 있다

print(player['friend']['name']) # 딕셔너리 안의 딕셔너리를 가져올 때 두 개를 써준다
print(player['friend']['age'])
# 직접 대괄호 안에 키를 써서 가져왔다. 이건 레나 아님
print(player['name'])

# 데이터를 업데이트하는 방법
player['fav_food'] = "apple"
# 이렇게 하면 원래 튜플이었지만, 이젠 튜플이 아닌 애플이 될 것이야. 추가가 아닌 업데이트다

# 데이터를 지우는 방법
player.pop('alive')

# 딕셔너리 안의 리스트를 업데이트하는 방법
player['friend']['age'].append("24") # friend 안의 age가 리스트란 걸 안다. 메소드 사용
# 리스트가 아니면 메소드를 사용할 수 없다. 명심!
print(player) """

# 3 5 For loops

websites = (
    "google.com",
    "airbnb.com",
    "naver.com",
    "daum.net"
)
# 한 줄로 코드를 작성하는 게 답답하다면 줄을 바꿔서 작성할 수 있다
# 이 튜플에 있는 웹사이트가 동작중인지 내려갔는지 확인할거야
# 여기서 알아야 할 것, 파이썬한테 튜플 안에 있는 각각의 아이템을 사용해서 코드를 실행하는 법

# websites[0] 이런 식도 가능하지만, 너무 오래 걸리고 아이템이 더 많으면 곤란하다
# 그래서 리스트의 각 아이템을 활용해서 자동으로 코드를 실행하라고 해야 한다
# 이걸 위해 for 반복문을 사용한다
# 주의할 점, 반점으로 데이터를 구분하지 않으면, google.com 글자 하나씩 헬로를 출력한다

for each in websites :
    print("hello")
 
# 첫 번째 핵심
# 각각의 웹사이트에 대해 코드를 실행하라고 했으며, 작동했다. 각각의 아이템에 코드를 실행할 수 있다!
# 즉 for 반복문은 각 아이템에 대해 코드를 실행한다. 프린트가 네 번 실행된 것이다

# 튜플 뿐 아니라 리스트에도 똑같이 작동한다
# 현재 처리 중인 아이템은 무엇일까?
# 다섯 번 실행된다면 리스트 내 어떤 아이템을 작업하고 있는지 알고 싶다

# for은 각각의 아이템이 사용될 때 플레이스홀더 만들기를 허락해준다
for potato in websites :
    print("potato is good so play", potato)

# 첫 번째 실행될 때 potato는 구글 두 번째는 에어비앤비, 순서대로 작동한다
# 현재 처리 중인 아이템이 무엇인지 알 수 있고, 어떤 집합체라도 이렇게 코드를 각각 실행할 수 있다
# 리스트나 튜플엔 복수형을 사용하는 게 관습이긴 하다
# for in에는 단수형 in 복수형 이런 식으로 한다. 이게 편하니까, 근데 뭐 내가 정하는 대로 해도 된다

# 3 6 URL Formatting

websites = (
    "google.com",
    "https://airbnb.com",
    "https://naver.com",
    "daum.net"
)
# https가 붙어 있으면 바로 이동하고 그렇지 않으면 지운다
# 무엇이 참인 지 확인해보자.

for website in websites :
    if website.startswith("https://") :
        print("good to go")
    else :
        print("we have to fix it")    

# if문은 true or false인지만 판단한다. 위에서 웹사이트가 https로 시작하는지 아닌지
# 이제 good to go를 출력하지 않는 https로 시작하지 않는 걸 판별
# if 뒤에 not을 붙인다

for website in websites :
    if not website.startswith("https://") :
        website = f"https://{website}" # 변수를 업데이트한다. f"" 잊지마라
        print(website)
# if not은 wensite가 https로 시작하는가? 값이 false와 같다고 표현하는 것과 마찬가지
# https가 붙지 않았다면 have to fix하라


OTT = ["netflix", "watcha", "wave", "disney"]

for company in OTT :
    if not company.endswith("x") :
        company = f"Don`t subcribe this {company}"         
        print(company)
        
# 3 8 Requests
# 파이썬 스탠다드 라이브러리에 없는 모듈을 써보겠다
# pypi를 사용하는 방법

# request라는 pypi를 사용할 것
# 나의 파이썬 코드에서 웹사이트로 리퀘스트 보내는 걸 하게 해준다
# 리퀘스트란 내가 구글로 이동하는 것이다. 구글 서버에 리퀘스트를 보내고 구글이 나에게 주소를 보내준다
# get은 function, 이동한 다음에 website를 가져온다

# 3 9 Status codes














