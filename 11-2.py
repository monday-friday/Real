# 순위 매기기
"""
import pandas as pd
 
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)
"""


"""  
# df["average"] = df.postcode.rank(method="average")
# print(df[["postcode", "average"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "dense"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max", ascending=False)
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "average"]])
"""

# 전치 컬럼-로우 변환
"""
print(df.transpose())
"""

# 누적 계산
"""
print(df["postcode"].expanding().sum())
"""

# 정렬 찾기
"""
# 가장 작은수
print(df.postcode.idxmax(axis=0))
# 가장 큰수
print(df.postcode.idxmin(axis=0))
"""

# 빈 Dataframe 확인
"""
print(df.empty())
"""

# 인자 검색
"""
print(df.isin([85576]))
"""
 
# 기간 계산
"""
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf)

i = pd.date_range("2023-11-10", periods=10, freq="1H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)
# 특정시간 인덱스 찾기
print(df.at_time("09:00"))
# 시간 범위 출력
print(df.between_time(start_time="12:00", end_time="00:00"))
"""
  
# 시간간격 데이터 
"""
import FinanceDataReader as fdr
import plotly

ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n----------------------\n")

# 최고가 확인
print(ksp["High"].max())
print("\n----------------------\n")
print(ksp["High"].idxmax())
print("\n----------------------\n")

# 최저가 확인
print(ksp["Low"].min())
print("\n----------------------\n")
print(ksp["Low"].idxmin())
print("\n----------------------\n")
print(ksp["Volume"].nsmallest(n=5))

# 최고가 값 찾기
print(ksp["Volume"].nlargest(n=5))
print("\n----------------------\n")

# 최하위 값 찾기
print(ksp["Volume"].nsmallest(n=5))
print("\n----------------------\n")

# kospi 3000 달성 최초일 찾기
cond = ksp["Close"] >= 3000
print(ksp[cond].index[0])
print("\n----------------------\n")

# 위(shift) 값 참조, 처리
print(ksp["Volume"] > ksp["Volume"].shift())
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
print(ksp)

ksp["grp"] = (ksp['up'] != ksp["up"].shift()).cumsum()
print(ksp)

# 연속 증가값 확인

ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).count() + 1
print(ksp)

print(ksp["up_cnt"].max())
"""

# 부동산 정보 처리
# 별
# 변환
"""
import pandas as pd

target = './data/apt.csv'
df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head()) 
"""

# 컬럼명 바꾸기
"""
df = pd.read_csv("./data/conv_apt.csv", index_col=0)
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)
 
arr = df.to_numpy()
# print(arr)
# print(len(arr))

# print(df.describe())

print(df.transpose())
print(df.T.head())
"""