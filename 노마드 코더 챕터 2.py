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

# 위에서 정의해준대로 값이 나온다. 당연하다
# if와 else의 안쪽에 넣어줘야 함을 기억하자. 
# 항상 else를 쓸 필요는 없다. 선택사항이다. if와 else가 합쳐진 게 elif
# 위의 두 개는 각각 한 가지 조건만 판단한다. 다른 조건도 확인하고 싶다면?

winner = 10

if winner > 10 :
    print("winner is greater than 10")
elif winner < 10 :
    print("winner is less than 10")
else :
    print("winner is 10")   

# elif는 코드에 대한 대안과 원하는 조건을 제공, else는 조건이 true가 아닐 때만 오직 대안을 제공한다
# 둘 다 항상 사용해야 하는 건 아니다

# 2 2 Recap
# else는 false일 때 실행하고 싶다면 넣어보자
# 조건식엔 =이 아니라 ==로 써야 한다. 변수 정의가 아니기 때문에
# != 는 같지 않다는 의미
help = 119

if help == 119 :
    print("wait")
else :
    print("stop")

you = 3000

if you != 3000 :
    print("AA")
elif you < 3000 :
    print("CC") 
elif you > 3000 :
    print(22)    
else :
    print(12)    
      
# elif는 여러 개 넣을 수 있다
# 파이썬은 조건이 트루인 걸 발견했다면 뒷부분은 실행하지 않는다.
# 조건을 따라가면서 True가 없다면 else 실행, 다시 말하지만 항상 모든 걸 사용할 필요는 없다
# elif가 True라도 if가 True라면 if만 실행된다

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
input("How old are you")






