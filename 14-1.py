""" # 다중그래프

import matplotlib.pyplot as plt

# 사용데이터
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

plt.subplot(2, 1, 2)
# plt.subplot(1, 2, 2) 
# plt.subplot(2, 2, 2)
# plt.subplot(3, 1, 1)
# plt.subplot(3, 1, 3)

plt.title("X1 Graph")
plt.xlabel("x2_data")
plt.ylabel("y2_data")

plt.plot(x1, y1, "o-")
plt.plot(x2, y2, ".-")


plt.subplot(3, 1, 1)
plt.subplot(3, 1, 2)
plt.subplot(3, 1, 3)

plt.plot(x1, y1, "-")
plt.plot(x2, y2, "-")




plt.subplot(2, 2, 1)
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)


plt.title("X3 Graph")
plt.xlabel("x4_data")
plt.ylabel("y4_data")

# 스타일 지정

plt.style.use("solarize_light2")
plt.tight_layout()

# 결과 이미지 저장

plt.savefig("data/img.jpg")
# plt.savefig("data/img.png")

plt.show()


# 다중 객체를 이용한 막대 그래프 출력

x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)

plt.tight_layout()

# 각 막대 그래프 설정 변경


ax4.bar(x_years, y_data, color = "red", edgecolor="black", hatch = "\\")
ax4.bar(x_years, y_data, color = "salmon", edgecolor="black", hatch = "+")
ax4.bar(x_years, y_data, color = "yellow", edgecolor="black", hatch = "/")
ax4.bar(x_years, y_data, color = "skyblue", edgecolor="black", hatch = "*")

plt.tight_layout()
plt.show()


# 생성 위치 지정

fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2)

# Seaborn 사용

import seaborn as sns
import pandas as pd
import FinanceDataReader as fdr


tips = sns.load_dataset("tips")
print(tips)

# 각 지표별 상관관계 출력
sns.regplot(x="day", y="tip", data=tips)
sns.regplot(x="day", y="total bill", data=tips)
sns.regplot(x="tip", y="total bill", data=tips)
sns.regplot(x="sex", y="total bill", data=tips)
sns.regplot(x="day", y="total bill", data=tips)
sns.regplot(x="smoker", y="tip", data=tips)
sns.regplot(x="smoker", y="total bill", data=tips)


plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("y")

plt.show()


# 타이타닉 데이터

titanic = sns.load_dataset("titanic")
print(titanic)

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)
plt.show()

# 탑승클래스별 인원구성
# sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
# sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
# sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
# sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
# sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)

plt.show()

# 주식 데이터 분석

import FinanceDataReader as fdr

df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

print(df0)

df0["Open"].plot()
df0["Close"].plot()
df0["Low"].plot()

plt.grid(True)
plt.show()



# 다우지수와 코스피 비교

dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# 각 지수별 종가 기준 그래프 출력
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

# 최고가 기준
plt.plot(dow.index, dow.High, "r--", label="Dow")
plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

# 해당 날짜 기준 종가 상승률, 상대 수익율 계산
d = (dow.Close / dow.Close.loc["2010-01-01"]) * 100
k = (kospi.Close / kospi.Close.loc["2010-01-02"]) * 100
plt.plot(d.index, d, "r--", label="Dow")
plt.plot(k.index, k, "b", label="KOSPI")

# 국내 개별 종목 분석
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

# 국내 주식 코드 확인
# 해당 데이터를 가져오는 URL
# code 는 종목명
url = "https://finance.naver.com/item/sise_day.nhn?code={}"

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

# 해당 사이트 1~100페이지 파싱
df_list = []

page = 1
for page in range(1, 100):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break

print(df_list)


# 데이터 처리

df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.plot(df["날짜"], df["종가"], "co-")
plt.title("Target(close)")
plt.xticks(rotation=45)
plt.grid(color="gray",linestyle="--")
plt.show()

# ticker 확인
import yfinance as yf
#MS
ticker = "MSFT"

# Apple
ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

# 시각화
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Close Price")


# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()


plt.plot(data["MA_50"], label="50-day Mean Average")
plt.plot(data["MA_200"], label="200-day Mean Average")

soup = BeautifulSoup(response.text, "html.parser")


rows = soup.select("example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))  
    countries.append(country)
    populations.append(population)


# 상위 10개 국가 시각화

top_countries = countries[:10]
top_populations = population[:10]


plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Close Price")

plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show()


 """