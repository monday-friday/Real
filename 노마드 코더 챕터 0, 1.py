# chpater 1 

# 1 0
# Hello, World!

# 1 1
# variable 변수

a = 2
b = 3
c = a + b
a = 10
b = 2 # 영향을 주지 않는다. 앞에서 이미 값을 도출해서 냈기 때문. 파이썬은 위에서 아래로
print(c)

# 변수엔 공백이 들어가지 않는다
# 숫자나 특수문자로 시작하는 변수는 없다. 반드시 문자로 시작
my_Age = 25
myage = 24

# 1 2
# 데이터의 종류

a = "Gogo" # 따옴표가 없으면 그걸 변수라고 인식한다. 문자라고 알려주기 위해 따옴표!
print(a)
b = "12" # 요것도 문자다
print(b)

# boolean 데이터 true or false
귀찮다 = True # 따옴표 붙이면 안 된다. 변수에 T or F를 입력하는 과정임을 기억하자
print(귀찮다)
# 불 데이터를 쓰는 이유는 뭐 죽었거나 살았거나? 
dead = False # 따옴표는 붙이면 안 된다
life = True # on , 1 등등 반대로 false는 o, off 등

# 1 3 Recap

print("Hello", 귀찮다)
print("and i am", dead, life)
# 앞에서 변수로 정리했다면 따옴표 따위는 필요 없다. 따옴표는 문자 데이터로 인식시키기 위해 필요한 것

# 1 4 function
# print 같은 거
# 펑션은 Def로 정의한다. 파이썬에서 펑션을 만들려면 def 를 써야 한다
# 여기도 마찬가지로 숫자로 시작하거나 공백이 있으면 안 된다
def say_hello(arr) : 
    print("hello how r u?")
    
def incheon(number) :
    print(number)    
# 여기까진 아무 일도 벌어나지 않는다. 펑션을 정의한 것이 다기 때문이고 펑션을 사용하지 않았기 때문이다
# 다른 말로 표현하면 정의했지만 호출하지 않았다
say_hello(22)
say_hello("arr")
# 함수를 실행할 때 정의했던 arr을 적지 않아도 된다. 빈 칸만 아니면 된다.
# arr은 플레이스홀더가 거기에 넣을 데이터가 필요했을 뿐이다. 그대로 출력하고 싶다면 number처럼 적어주면 되고
# 그렇지 않다면 적어주지 않아도 상관 없다. 

incheon(12)
""" print 역시 펑션이다. 위의 세이 헬로 역시 마찬가지
print(1212) 처럼 내가 정의한 펑션 say_hello() 역시 마찬가지 """

# 펑션 옆의 빈 괄호는 플레이 버튼이라고 생각하면 된다. 안에 있는 코드를 실행하기 위해선
# 즉 def로 정의된 코드를 실행하기 위해선 빈 괄호를 옆에 적어줘야 한다
# 물론 def로 정의할 때의 빈 괄호의 의미는 실행이 아니다. 정의하는 것이니깐.
# 괄호 안에 있는 것은 즉 펑션 안의 코드를 실행하기 위함이다!

# 1 5 indentation
""" 
def say_hello() : 
    print("hello how r u?") """
# 들여쓰기가 없으면 파이썬은 공백을 이용해 어떤 것 안에 어떤 게 있는지 이해한다
# 즉 세이 헬로 안에 헬로 하우알유가 있다는 것을 알려주기 위해 들여쓴다

""" def say_bye() :
    print("bye")
    print("hello") """
# 이렇게 안에 넣으면 say_bye 안에 hello를 넣은 것, 즉 세이 바이를 실행하면 프린트, 세이 헬로가 둘 다 실행
# say_bye()

# def 아래에 들여쓴 게 없다면 펑션에 실행할 코드가 없다는 것이다. 들여써서 내용을 넣어주는 것이다

# 1 6 parameters
# 어떤 값이든 괄호 안에 넣으면 프린트 펑션이 가져가서 콘솔에 뿌려준다. 
# 펑션으로 도출한 값을 수정하는 방법

""" def say_hello() : 
    print("hello how r u?")
 """

say_hello("Gin")
# 이건 실행되지 않는다. 왜냐하면 gin을 위해 아무것도 쓰지 않았기 때문, 그래서 공간을 만들어준다
# 다시 말하자면 펑션을 만들 때는 데이터가 들어가는 플레이스홀더 같은 공간을 제공해야 한다

""" def say_hello(name) :
    print("hello", name, "wow another class")        """          

# 여기서 name은 parameter라고 한다. 아래의 르브론 진 등은 argument.     
""" say_hello("Gin")    
say_hello("durant")
say_hello("lebron")
 """
def shittheclass(class_name) :
    print("please fire", class_name, "stop talking")

shittheclass("mijeongp")

# Gin이라는 데이터를 name의 값으로 주겠다
# 내가 준 gin이라는 값을 받을 거고 그건 name에 저장된다
# 문자 데이터가 아니므로 따옴표는 넣지 않는다(function 내 class_name 말하는 거다)
# 공백과 달리 name은 첫번째 인자로 어떤 데이터를 원한다! gin 같은
# name이라는 플레이스 홀더는 펑션 안에서 쓸 수 있는 변수다. print(name)을 밖에 쓰면 유효하지 않다
# 밖에서 부를 때 당연히 따옴표는 붙여야 한다. 없으면 또 다른 변수 정의가 필요하다

# 1 7 multiple parameters
# 데이터, 데이터 이런 식으로 우리가 만든 함수에도 콤마를 찍고 싶다!
# parameter로 가서 콤마를 찍어준다! 그릇을 여러 개 만들어준다고 생각하자

def nba_player(team, name) :
    print(team, name, "is a winner in 2023")
    print("He is a world champion")
    
# 여기서 그릇을 두 개 만들었고 이는 쉿더클래스 함수는 2개의 데이터를 받는다고 정의했기 때문이다
# 필요한 데이터를 모두 보내줘야 하니까, 두 개를 써주자. 순서도 고려해서
nba_player("phoenix", "booker")
nba_player("golden states", "curry")

# argument는 그럼 몇 개를 줄 수 있는가? 플레이스홀더 개수 만큼이다. 
# 무한대로 쓸 수 있지만, 실제 제작자들이 그러진 않았을 것. 뒷부분에서 한다


# 1 8 Recap
# 펑션은 함수, 함수를 복습해보자

def tax_calculator(bank) :
    print(3000 * 3, bank, "exchange")

tax_calculator("kookmin")
tax_calculator("sinhan")

def self_calculator(math) :
    print(math, "quiz")
    
self_calculator("high school")    

# 1 9 default parameters

# 유용한 정보
# 앞서 Argument가 없으면 에러가 뜬다. 그러나 에러가 아닌 예를 들어 Hello 아무개 혹은 익명 어쩌고로 만들 수 있는 방법
# 바로 parameter에 기본값을 정해주는 것

def say_hello(user_name="tom") :
    print("Hello", user_name)

say_hello("king")
say_hello()

def musician (music = "post malone") :
    print(music,"is my favorite")
    
musician("Yerin")    
# parameter에 '=기본값'을 써준다. 이퀄을 붙여주는 것!

# 챌린지! 계산기를 만들어보자
# 사용자들이 실수했을 때를 대비해 에러가 아닌 기본값을 보여준다

def plus(a = 1,b= 2) :
    print(a + b)

plus(7, 3)

def minus(a=1, b=0) :
    print(a - b)
    
minus(10, 2)

def multiply(a= 2, b = 0) :
    print(a * b)
    
multiply(9, 12)

def divide(a= 1, b= 1) :
    print(a / b)
    
divide(12, 2)

def powerof(a = 2, b = 3) :
    print(a ** b)
    
powerof(8, 8)

plus()
minus()
multiply()
divide()
powerof()                

# parameter이 두 개라면 두 개 모두 기본값을 지정해줘야 한다. 그래야 에러가 나오지 않는다
# 기본값은 어쨌든 식이 성립할 수 있는 요소가 들어가야 한다. 문자열을 제곱할 수는 없으므로
# 0으로 나누는 식 역시 안 된다

# 1 10 Return Values
# 여기선 함수로부터 값을 받는 것도 배워보겠다

def tax_calculator(money) :
    return(money * 2)

# 위 함수의 결과를 받아서 나중에 내 코드에 쓰고 싶다면?

def pay_tax(tax) :
    print("thank you for paying", tax)

love = tax_calculator(2000)
pay_tax(love)

# 만약 여기서 계산값을 페이 택스로 불러오고 싶다면 값을 복사해야 한다
# 이건 비효율적, 함수에서 무언가를 받아오는 법을 배우자
# 함수는 주스 기계, 데이터가 과일! 그게 리턴이 하는 역할이다 주스를 만들어준다
# 프린트를 리턴으로 바꾼다
# 2000이 과일이고 택스 계산기가 주스 기계, 그리고 4000이 주스인 것이다

gongcha = tax_calculator(2000)
pay_tax(gongcha)

# 다시 말하면 리턴은 곧 결괏값인데, 이는 다르게 정의할 수 있다는 것이다 프린트는 to_pay같은 곳에
# 결괏값, 즉 주스를 저장할 수 없다. 리턴의 의미는 함수 바깥으로 값을 보낸다는 것이다

pay_tax(tax_calculator(2000))

# 더 짧게 하려면 이렇게 써도 된다. 리턴은 값을 보관한다. 명심하자
# 프린트는 콘솔에서 값을 확인하는 거고, 리턴은 함수 바깥으로 값을 보낼 수 있게 해준다

def personal_color(choice) :
    return(f"{choice} is for you!")

def dress_color(want) :
    print(want, "perfect!")

fashion = personal_color("yellow")
dress_color(fashion)


#1 11 Return Recap

# 문자열 안에 변수를 넣는 기능
my_name = "kim"
my_age = 24
my_movie = "Intern"

print(f"Hello i`m {my_name}, i have {my_age} years in the earth, {my_movie} is my art")

a_list = "god"
b_list = "please"

print(f"dont stop me now, {a_list}, {b_list}, haha")

adobe = "photoshop"
print(f"you should learn {adobe}")

# 위처럼 중간에 쌍따옴표를 넣지 않도록 주의한다
# 만약 문자 데이터를 그냥 통째로 출력하고 싶다면 앞에 f를 써주고 뒤에 쌍따옴표를 붙인 뒤 중괄호를 씌워 입력해준다
# f를 써주지 않으면 그냥 중괄호까지 그대로 출력한다

# 주스를 만들고 설탕과 얼음을 넣는다고 생각하자

def make_juice(fruit) :
    return f"{fruit} + juice"

def add_ice(juice) :
    return f"{juice} + ice"

def add_sugar(iced_juice) :
    return f"{iced_juice}+ 슈거"

juice = make_juice("lemon") # lemon + juice
print(juice)
iced_juice = add_ice(juice)# leomon + juice + ice
print(iced_juice)
lemonade = add_sugar(iced_juice) # lemon + juice + ice + 슈거

print(lemonade)

# f를 붙이느냐 않느냐의 차이
# 붙이면 lemon + juice를 문자열 그대로 출력하지만 안 붙이면 +가 적용되어 lemonjuice가 된다
# 이말인즉슨, 뒤의 정의되지 않는 문자 데이터에 쌍따옴표를 붙여야 하고, 빼기, 곱하기 등은 안 된다   
# 중괄호를 붙이지 않으면 앞의 값을 문자열 그대로 출력하지 않는다
# return은 값을 가지고 함수 바깥으로 던져주고 파이썬은 그걸 잡아 코드에 대입해준다!    
# return은 함수를 끝낸다 즉 뒤이어 프린트든 뭐든 적어도 실행 안된다. 리턴값이 놓인다

def usa_region(name) :
    return(f"{name} + lakers")

def basketball(team) :
    return(f"{team} + player")

def people(player) :
    return(f"{player} + is Anthony Davis")

american = usa_region("La")
print(american)
center = basketball(american)
print(center)
my_pic = people(center)

print(my_pic)

# 위에서 american, center처럼 함수 내 플레이스홀더와 다르게 하는 이유는 구분하기 위함이다
# 똑같다면 식을 진행할 때 구분하기 힘들기 때문이다.

# 첫 식에서만 정의되지 않았으므로 문자데이터, 쌍따옴표 붙여주고 뒤에선 정의되었으므로 안 붙여줘도 된다
# 마지막으로 fourth를 프린트할 것이므로 여기까지 정의가 돼야 한다