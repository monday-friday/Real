""" import asyncio
import random as rd

async def tester(name) :
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum) :
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
    
    print(f"end of {name}")
        
async def main() :
    task1 = asyncio.create_task(tester("1test"))   
    
    task2 = asyncio.create_task(tester("2test")) 
     
    task3 = asyncio.create_task(tester("3test"))      
        
    print("start") 
    await task1    
    await task2 
    await task3
    print("end")
    
if __name__ == '__main__' :
    asyncio.run(main())    """    
       
""" import asyncio      
import time  
   
async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)

async def worker2() :
    for i in range(1,4):
        print(f"Task 2 : Step {i}")
        await asyncio.sleep(1)

async def main() :
    
	task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    stat = time.time()
    await task_1
    await task_2
    end =  time.time()
    print("end task")


if __name__ == '__main__' : """

# 스케줄

""" import time
import sched

start = time.time()

def tester(name) :
    print(f"start.time{time.time() - start}")
    for i in range(3) :
        print(f"{name} - {i}")
    
    print(f"end of {name}") 


def run() :    
    s = sched.scheduler()
    s.enter(5,1, tester, ('1num'))       
    s.enter(3,1, tester, ('2num'))  
    s.enter(7,1, tester, ('3num'))  
    s.run()    

if __name__ == "__main__" :
    run()
    #main()
    print("end")
 """
    
# 문자열 비교
""" 
import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, that is a answer!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """


# faker 임의 데이터

""" from faker import Faker as fk

temp = fk()
print(temp.name())

# temp = Faker("ko-KR")

print(temp.name() + "\n" +
      temp.address() + "\n" +
      temp.postcode() + "\n" +  
      temp.country() + "\n" +
      temp.company() + "\n" +
      temp.job() + "\n" +
      temp.phone_number() + "\n" +
      temp.email() + "\n" +
      temp.user_name() + "\n" +
      temp.ipv4_private() + "\n" +
      temp.catch_phrase() + "\n") """

# with open("fktemp.csv", "w", newline='') as f :
""" with open("fktemp.txt", "w", newline='') as f :    
    for i in range(30) :      
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")      """   
""" 

import subprocess as sp


res = sp.run(["cmd", "/c", "dir"], capture_output=True)
# print(res)
s = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
print(res)
 """
# 에러처리
import traceback as tb

def tester() :
    return 1

def caller() :
    tester()
    
def main() :
    try : 
        caller()
            
    except ZeroDivisionError:
        print("zde error")
	# 0을 나누어 에러 발생시 처리

    except ValueError :
        print("ve error")
	# 유효하지 않는 정수를 입력했을시 처리

    except Exception as ex :
        print("ex error", ex)
	# 모든 예외를 처리할때 처리

    else :
        print("ok")
	# 에러가 없으면

    finally :
        print("end")
	# 해당 함수가 에러가 있든 없든, 완료될때 처리


# 데이터 생성

# HTML
# 웹은 다 html인데 그걸 파싱해서 데이터를 가져와야 함. 파싱이란 데이터를 쪼개서 가져오는 것
# 디자이너 프론트엔드, 백엔드 이렇게 세 가지만 있으면 된다. 한 명이 여러가지 일을 할 수 도 있다
# 그냥 뭐 이런 것들이 있다. 데이터 예제 코드 개발자 엘레멘트에 붙이면 시각화됨 데스크탑으로 해보길
# f12누르고엘레멘트 찾아라, 거기에 예제 넣어
# CSS

# 웹크롤링

from bs4 import BeautifulSoup as bs
import requests as rq

# url = "https"//xkcd.com/2852/
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.parser")

pres = res_html.find("h2")
print(pres)
print("\n1 -------------------- \n")
print(pres.get_text().strip())
print("\n2 -------------------- \n")
print(pres.next_element.get_text().strip())
print("\n5 -------------------- \n")
print(pres.get_text())


tres = res_html.find("title")
print(tres)
print("\n1 -------------------- \n")
print(tres.next_element)
print("\n3 -------------------- \n")
print(tres.get_text().strip())



fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
        
# print(fares)
print("\n5 -------------------- \n")

clres = res_html.findAll(class_  = "doc - title")
print(clres)

print("\n6 -------------------- \n")
clrs = res_html.find(class_ = "head_top")
print(clrs)
print(clrs.get_text())

# 어쨌든 궁금한 내용을 찾아서 가져오는 거임 뉴스 연예 스포츠 등등 기존의 웹페이지에서 가져오는 것

# 셀렉터로 찾기


""" from bs4 import BeautifulSoup as bs
import requests as rq

# url = "https"//xkcd.com/2852/
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.parser")

item = res_html.select_one("body > div.container-doc")

print(item)
print(item.get_text())
print("\n90----------------\n")
print(item)
print(item.get_text().strip())

print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
#print(wt)
# print(wt.get_text())


goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
# print(goods.get_text()) """

# select

from bs4 import BeautifulSoup as bs
import requests as rq

# url = "https"//xkcd.com/2852/
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.parser")

iss = res_html.select("a.wrap_thumb")

print("\n--------------------\n")

for i in iss :
    issue = i.get_text()
    print(issue)
    
print("\n----------------\n")   
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs["data-tiara-custom"] 
    print(c + "\n")   


