""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

print(item)
print(item.get_text())

#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text())

# select
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumbs")
# print(iss)

print("\n================\n")
for i in iss :
    issue = i.get_text()
    print(issue)
    
print("====")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    # c = j.attrs["data-tiara-custom"]
    c = j.attrs["data-tiara-id"]
    print(c + "\n")
    
    
# 이미지 url
    
from bs4 import BeautifulSoup as bs
import requests as rq

import os
from urllib.request import urlretrieve as rl

url = "https//news.daum.net/" 
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')   
    
imgs = res_html.select("img")
print(imgs)

linkimgs = []
for i in imgs :
    irs = i.attrs["arc"]
    linkimgs.append(irs)  
    
folder = "imgs/"
if not os.path.isdlr(folder) :
    os.mkdir(folder)
    
i = 0
for In in linkimgs :
    if str(In).find("//t") == False :
        print(In)
        continue
    else :
        pass
    
    i == 1
    rl(In, folder + f"{i}.jpg")          
    
 """

# 시리즈 생성

from pandas import Series as sr
""" 
data = [10, 20,30, 40]
sdata = sr(data)
print(sdata) """


""" import numpy as np

data = np.arange(1, 5)
sdata = sr(data)
print(sdata)


# 인덱스 확인

from pandas import Series as sr

data = [10, 20, 30, 40]
sdata = sr(data)

print(sdata.index)
print(sdata.index.to_list())


# 인덱스 설정

from pandas import Series as sr

data = [10, 20, 30, 40]
sdata = sr(data)
print(sdata)
print("===============")

sdata.index = ["A", "b", "c","d"]
print(sdata)


# 인덱스 생성 

from pandas import Series as sr

dt = [10, 20, 30, 40]
idx = ["a","c","d","e"]
       
sdata = sr(data=dt, index=idx)
print(sdata)       


sdata = sr(idx, data)
print(sdata)




from pandas import Series as sr

dt = [10, 20, 30, 40]
idx = ["a","c","d","e"]
       
sdata = sr(data=dt, index=idx) 

# sd = sdata.reindex(["a", "j", "c"])
# sd = sdata.reindex(["a", "j"])

# print(sd)

sd = sdata.reindex(["b"])
print(sd)
print("==============")
print(sdata["b"])
print("==============")

print(sdata.iloc[0])
print(sdata.iloc[2])

print("==============")

print(data.loc["a"])
print(data.loc["j"])   


# 슬라이싱

from pandas import Series as sr

dt = ["aa", "dd", "cc", "ff"]
idx = ["fd", "ad", "rh", "dfd"]

sdata = sr(data=dt, index=idx)

print(sdata.loc["fd : ad"])
print("==============")

print(sdata.loc["fd"])
print("==============")

print(sdata.loc["rh"])
print("==============")

# 인덱싱 행번호

from pandas import Series as sr

dt = ["가", "나", "다", "라"]
idx = ["마", "바", "사", "아"]

sdata = sr(data=dt, index=idx)

print(sdata.iloc[1:2])

print(sdata.iloc[2 :])

print(sdata.iloc[:2])


# 인덱스 슬라이싱


from pandas import Series as sr

dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data=dt, index=idx)

sdata.loc["cd"] = "echo"
print(sdata)

print("===============")

sdata.iloc[1] = "fox"
print(sdata)


sdata.loc["ef"] = "golf"
print(sdata)

sdata.drop("bc")

sd = sdata.drop("cd")
print(sd)



from pandas import Series as sr

s1 = sr([100, 200, 300], index = ["a", "b", "c"])
s2 = sr([100, 200, 300], index = ["b", "c", "a"])
       
sum_res = s1 + s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print(sum_res.min())

print("======================")       

mul_res = s2 + 10
print(mul_res)

dv_res = s1 /10
print(dv_res)



data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unique()
print(uniq)

sc = sdata.count()
print(sc)

sv = sdata.value_counts()
print(sv)



# 필터링

idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

# 시리즈내 데이터 비
fil = s1 > 300
print(fil)

print(s1[fil])
print(s1[fil].index)

# 시리즈간 비교
fil1 = s2 > s1
print(fil1)
print(s2[fil1].index)


# 인덱싱 출력
s2[s2 > s1].index
print(s2[s2 > s1].index)



# 정렬

from pandas import Series as sr


idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
s1 = sr(data=dt, index=idx)
       
       
sv = s1.sort_values()
print(sv)

sv1 = s1.sort_values(ascending=False)
print(sv1) """






