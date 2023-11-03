""" import calc as cm

# print(cm.calc.add(1,2))

cl = cm.calc()

print(cl.add(1,2))
"""

# 문자열 처리

# 줄임말 처리

import textwrap as tw

targetText = "9시"
res = tw.shorten(targetText, width=20)

print(res)


# 줄 바꿈 처리

""" import textwrap
textwrap.wrap()
 """
""" import textwrap as tw
target = "out of time"
longtarget = target * 2

print(longtarget)
print("\n=======\n")

song = tw.wrap(longtarget, width=2)
print(song)

print('\n'.join(target))

print("\n====\n")
rs = tw.fill(longtarget, width = 50)
print(rs)

 """
# 문자열 치환
""" 
line = "홍길동의 주민번호는 012345-1234567 입니다. "
word_result = []

for word in line.split(" ") :
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
		    word = word[:6] + "-" + "*******"
    word_result.append(word) 
    
print(" ".join(word_result))    """



import re
line = "홍길동의 주민번호는 012345-1234567 입니다."
res = re.compile("(\d{6}[-]\d{7})")

print(res.sub("g<1>-*******", line))

#주민등록번호 매칭 표현식

re.compile("(\d{6}[-]\d{7})")

# 치환

res.sub("g<1>-*******", line) 


# 날짜 처리

import datetime

# 날짜 출력
import datetime as dt

day1 = dt.date(2023, 11, 1)
day2 = dt.date(2022, 2, 8)

# 날짜 계산
diff = day1 - day2
print(diff)


# 날짜 객체1
res = dt.datetime(2023, 11, 1, 12, 30, 40)
thour = res.hour
tmin = res.minute
tsec = res.second

print(res, thour, " ", tmin, " ", tsec)

# 날짜 객체2
day = dt.date(2023, 11, 1)
time = dt.time(12, 30, 40)
hop = dt.datetime.combine(day, time)

print(hop, hop.hour, hop.minute)

# 요일 판별
import datetime as dt

day = dt.date(2023, 11, 1)
print(day.weekday())

yesterday = dt.date(2023, 10, 31)
print(yesterday.weekday())


# 날짜 세기
today = dt.date.today()
print(today)

difday = dt.timedelta(days = 110)
# difday = dt.timedelta(hours = 11)
# difday = dt.timedelta(minute = 20)

print(difday)

go = today + difday
print(go)

# 단어 세기

import collections

poem = """
내가 그의 이름을 불러 주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러 주었을 때
그는 나에게로 와서
꽃이 되었다.
내가 그의 이름을 불러 준 것처럼
나의 이 빛깔과 향기에 알맞은
누가 나의 이름을 불러 다오.
그에게로 가서 나도
그의 꽃이 되고 싶다.
우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다."""

""" wd = re.findall(r"\w+", poem)

print(wd)
print(len(wd))

# 많이 사용되는 단어 찾기

cnt = cl.Counter(wd)

print(cnt.most_common(1)) """


# 정렬 출력

import pprint

data = {"month": "9", "num": 642, "link": "", "year": "2009", "news": "", "safe_title": "Creepy", "transcript": "[[Two people are sitting on chairs.]]\nMan: Hey, cute netbook.\nWoman: \nWhat.\n\n\nMan: Your laptop. I just --\nWoman: No, why are you talking to me.\n\nWoman: Who do you think you are? If I were even slightly interested, I'd have shown it.\n\nWoman: Hey everyone, this dude's hitting on me.\nVoice #1: Haha\nVoice #2: Creepy\nVoice #3: Let's get his picture for Facebook to warn others.\n\n((This panel fades into a thought bubble of the actual man.))\n[[The girl is typing on her laptop.]]\nDear blog,\nCute boy on train still ignoring me.\n\n{{Title text: And I even got out my adorable new netbook!}}", "alt": "And I even got out my adorable new netbook!", "img": "https://imgs.xkcd.com/comics/creepy.png", "title": "Creepy", "day": "28"}
# print(data)
pprint.pprint(data)


# 수학 문제

import math

# 최대공약수
res = math.gcd(60, 100, 80)
print(res)

# 최소공배수
gong = math.lcm(15, 25)
print(gong)

# 로또 번호 생성
import random

res = []
while len(res) < 6:
    num = random.randint(1, 45)
    if num not in res:
        res.append(num)

print(res)

# 통계

import statistics

data = [48, 92, 57, 59, 63, 83, 56, 91, 82, 74, 63, 72]
res = statistics.mean(data)

print(res)

mid = statistics.median(data)

print(mid)

# 압축하기

import zlib

data = "Dunk!"
longData = data * 100

print(len(longData))
print("\n=======\n")
cmp = zlib.compress(longData.encode(encoding="utf-8"))
print(cmp)
print("\n========\n")
print(len(cmp))

# 압축 해제

decmp = zlib.decompress(cmp).decode("utf-8")
print(decmp)

print("\n============\n")
print(len(decmp))

# 파일 압축 저장

import gzip

# 압축 저장하기

""" data = "three point" * 10000
print(len(data))

with gzip.open('data.txt.gz', 'wb') as fp:
    fp.write(data.encode('utf-8')) """
"""
# 압축 읽기
with gzip.open('data.txt.gz', 'rb') as fp :
    read_data = fp.read().decode('utf - 8')
    print(read_data)
    
# 압축 2
import bz2

# 압축하기
data = "block shot!" * 10000
cmp = bz2.compress(data.encode(encoding="utf-8"))

print(cmp)
print(len(cmp))

# 해제하기

decmp = bz2.decompress(cmp).decode("utf-8")
print(decmp)
print(len(decmp))

# 파일 압축    

import zipfile as zf

# 압축하기
fp1 = open("a.txt", "w")
fp1.write(data)
fp1.close()

fp2 = open("b.txt", "w")
fp2.write(data)
fp2.close()

fp3 = open("c.txt", "w")
fp3.write(data)
fp3.close()

with zf.ZipFile('txt.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zf.ZipFile('txt.zip') as myzip:
    myzip.extractall()


# tar파일 압축

import tarfile
data = "Anckle Breaker"

fp1 = open("atar.txt", "w")
fp1.write(data)
fp1.close()

fp2 = open("btar.txt", "w")
fp2.write(data)
fp2.close()

fp3 = open("ctar.txt", "w")
fp3.write(data)
fp3.close()


with tarfile.open('txt.tar', 'w') as mytar:
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')
"""    

# tar파일 해제
""" import tarfile

with tarfile.open('txt.tar') as mytar:
    mytar.extractall()

 """

# 실행 아규먼트

import argparse
import functools

# 아규먼트 파싱
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')
parser.add_argument('-s', '--sub', type=int, nargs='+', metavar='N', help='뺄 숫자')
args = parser.parse_args()

# functools 모듈 활용

if args.add:
    print("총합 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("총곱 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))
if args.sub:
    print("결과 %d입니다." % functools.reduce(lambda x, y: x - y, args.sub))




