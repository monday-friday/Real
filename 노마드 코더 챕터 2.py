# 2 0 IF
# 조건문

if 10 == 10 :
    print("True")

# 반대로 틀린 걸 적었다면 아무것도 실행되지 않는다
# 하나의 등호는 특정 값을 특정 변수에 넣겠다는 것
# == 가 같다는 의미

# 2 1 Else & Elif

password_correct = False

if password_correct :
    print("here is your money")
else :
    print("dont touch me")

watermelone = 100

if watermelone > 50 :
    print("Summer is comming!")
else :
    print("Not yet")
# 위에서 정의해준대로 값이 나온다. 당연하다
# if와 else의 안쪽에 넣어줘야 함을 기억하자. 
# 항상 else를 쓸 필요는 없다. 선택사항이다. if와 else가 합쳐진 게 elif
# 위의 두 개는 각각 한 가지 조건만 판단한다. 다른 조건도 확인하고 싶다면? elif를 활용하자!

winner = 10

if winner > 10 :
    print("winner is greater than 10")
elif winner < 10 :
    print("winner is less than 10")
else :
    print("winner is 10")   

paul = 0
Curry = 3
James = 5

if Curry <= paul :
    print("pg goat is curry")
elif James == Curry :
    print("lbj is better than jordan")
else :
    print("Welcome to NBA")    

# elif는 코드에 대한 대안과 원하는 조건을 제공, else는 조건이 true가 아닐 때만 오직 대안을 제공한다
# 둘 다 항상 사용해야 하는 건 아니다

# 2 2 Recap
# else는 false일 때 실행하고 싶은 코드가 있다면 넣어보자
# 조건식엔 =이 아니라 ==로 써야 한다. 변수 정의가 아니기 때문에
# != 는 같지 않다는 의미
help = 119

if help == 119 :
    print("wait")
else : 
    print("stop") 
      
Top = 45

if Top < 30 :
    print("You are first!")      
      
# elif는 여러 개 넣을 수 있다
# 파이썬은 조건이 트루인 걸 발견했다면 뒷부분은 실행하지 않는다.
# 조건을 따라가면서 True가 없다면 else 실행, 다시 말하지만 항상 모든 걸 사용할 필요는 없다
# elif가 True라도 if가 True라면 if만 실행된다
# else를 적지 않았는데 if가 false라면 아무것도 출력되지 않는다

coffee = 2500
if coffee > 4600 :
    print("스타벅스")
elif coffee > 3500 :
    print("two some")
elif coffee > 2800 :
    print("Ediya")
elif coffee != 2500 :
    print("mega coffee")
elif coffee >= 2500 :
    print("compose")
elif coffee == 2500 :
    print("mammard")
else :
    print("home")

# 2 3 And & or
# 음주 가능 나이 계산기를 만들어보자
# 이를 위해 필요한 유용한 함수 세 가지

# input
# input은 오직 한 가지 argument만을 받는다
# 콘솔에 argu가 나온다. 하지만 단순 프린트가 아니다. 콘솔에서 질문에 대한 나의 답을 기다리고 있다
# 내가 콘솔에 답을 하면 그제서야 프로그램이 끝난다
# 즉 input으로 user에게 질문하면 user가 답을 하는 것이다
# input("Who is your favorite artist?") 두 번 적을 필요 없다. name에 인풋값을 저장해주었으면 그걸로 된 거다

# 사용자가 input에 답한 것이 함수의 return 값이다.
# 그래서 이 함수의 값을 저장해야 하고 이걸 age

""" name = input("Who is your favorite artist?")
print("artist", name) """

# age에 인풋의 질문에 대한 유저의 리턴값이 저장된 것

# type
# 변수의 type을 알려주는 함수
""" print(type(24))
print(type(True))
print(type("gottcha")) """
# 이 문자 데이터를 숫자로 변환하려 한다. 그 이유는 Age가 18보다 작은지 확인하고 싶기 때문
# age가 String이라면 18과 비교할 수가 없다
# 그래서 input 함수를 int 함수로 감싸주는 것이다

age = int(input("how old are you?"))

# 유저가 답한 인풋 안에 있는 건 문자 데이터다, 숫자라도 문자 데이터. 그래서 int 활용

if age < 18 :
    print("You can`t drink")
# 18세 이상이면서 35세 미만인 지 알아보자. and를 활용한다. and는 if, elif 둘 다 에서 작용
# 두 가지 조건을 확인 시켜준다. 모두 true여야 and가 true로 나온다    
elif age >= 18 and age <= 35 :
    print("you drink beer!")
elif age == 60 or age == 70 :
    print("Birthday party")
# or은 두 가지 조건 중 하나만 true면 전체 조건 역시 True
elif age == 22 or age == 33 :
    print("couple matching!")
elif age >= 30 :
    print("you should give two dollar")    
else :
    print("Go ahead!")  

"""score = int(input("Your goal"))
print("Good job you made ", score)


if score < 10 :
    print("I`m so sorry, you are fire")
elif score > 10 and score < 15 :
    print("Fine! I`ll give you bonus!")
elif score >=15 or score <=5 :
    print("Hey! What`s wrong with you?")
else :
    print("Okay you should think more second")            

 """
# 2 4 python standard library
# python 카지노를 만들 것이다

""" user_choice = int(input("choose number."))
from random import randint
 """
""" pc_choice = randint(1, 50) # randint(a , b)는 a와 b 사이 숫자 아무거나

if user_choice == pc_choice :
    print("You won!")
elif user_choice > pc_choice :
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice :
    print("higher! computer chose", pc_choice) """
    
"""    
user_number = int(input("give your number!"))

from random import randint

pachinko_number = randint(10,100)    

if user_number == pachinko_number :
    print("1 dollar")
elif user_number >= pachinko_number :    
    print("What a wonderful")
elif user_number <= pachinko_number :  # <= 작거나 같다, 이게 맞으니 헷갈리지 마라
    print("just get out") """
    
    
# else는 굳이 넣지 않아도 된다 이미 모든 경우를 보고 있기 때문이지
# 숫자를 우선 랜덤하게 생성해야 된다. 그럴려면 라이브러리를 한 번 보자
# 라이브러리란 기본으로 포함된 펑션, 즉 함수들이다
# built in function이란 항상 즉시 사용할 수 있는 것
# import는 이 수많은 함수들이 모두 built in처럼 항상 존재할 수 없기 때문에 불러오는 것
# 그래서 import 해온다! 예를 들어 나는 random module을 사용하고 싶다
# 이 랜덤 모듈엔 랜덤 숫자 생성과 관련된 많은 함수가 있다
# 우리는 이중에서 randint, 랜덤한 정수를 주는 이 function을 가져올 거다. 어떻게 쓰지?
# random은 모듈의 이름이다. 랜덤 모듈에서 from! randint function을 import 한다!
# 참고로 random이라는 이름의 function도 있다. 헷갈리지 말자
# 컴퓨터가 고른 번호를 볼 수 있도록 print를 바꿔준다

# 2 5 while
# 또 다른 조건문, 중지할 때까지 계속 동작한다
# while은 if와 같다, 멈추지 않는다는 점만 빼고

""" while True :
    print("ok!") """
    
# 여기서 if는 한 번만 작동하지만 while은 계속 작동한다, 즉 if일 경우 True 한 번만 나오지만 while은 계속 나온다
# while은 조건 true이면 이 코드를 실행시키지만, 거기서 또 실행한다.
# 그래서 멈추기 위해선 false로 바꿔야 한다

distance = 0

while distance < 20 :
    print("i`m running:", distance, "km")
    distance = distance + 1
# +1을 해주면서 결국 20이 되기 전에 멈춘다

want = 1

while want < 30 :
    print("just do it", want)
    want = want + 5


# 2 6 python casino
# pc_choice = randint(1, 50) randint(a , b)는 a와 b 사이 숫자 아무거나

from random import randint

print("Welcome to python Casino")
pc_choice = randint(1, 100)

playing = True

while playing :
    user_choice = int(input("choose number."))
    if user_choice == pc_choice :
        print("You won!")
        playing = False
    elif user_choice > pc_choice :
        print("Lower!")
    elif user_choice < pc_choice :
        print("higher!") 

print("Welcome to russian rullet")

my_choice = randint(1,3)

game = True

while game :
    your_choice = int(input("Hey, your turn."))
    if your_choice == my_choice :
        print("lucky guy, go home.")
        game = False
    elif your_choice > my_choice :
        print("too much guy") 
    elif your_choice < my_choice :
        print("it`s over. byebye.")       


# 이 코드를 유저가 이길 때까지 계속 반복하고 싶어. 이 코드를, You won이 실행될 때까지
# 위처럼 탭으로 들여 쓰면 while 안으로 포함된다
# 위에서 playing이 True라면 while은 계속 반복된다. 즉 playing을 False로 바꿔줘야 한다
# 즉 유저가 이긴다면 플레잉은 그 즉시 False가 된다

# 2 7 Recap
# if와 while 차이
# 모듈은 파일이라고 생각하면 된다
# if는 한 번만 실행! while은 조건문이 true라면 계속해서 실행, 멈추는 게 나의 의무!

movie = False

# while 조건문에도 or true나 and 또한 쓸 수 있다
# if에 썼던 것들을 다 쓸 수 있다

while movie and True :
    print("Academy")
    movie = False
else :
    print("lazberry")

    
worldcup = True    
brazil = 1
germany = 2
france = 3
korea = 4    
    
while worldcup :
    your_select = int(input("hey give me number"))
    if your_select == brazil :
        print("What the fxxx! you are 매국노")
    elif your_select == germany :
        print("hey you are 전범?")
    elif your_select == france :
        print("you are not 파리지앵") 
    elif your_select == korea :
        print("you are 독립투사!")
        worldcup = False
        








