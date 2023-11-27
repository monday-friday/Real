""" # 변환

import pandas as pd

df= pd.read_csv("./data/apttt.csv", index_col=0)

print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})

df["분양가"] = df["분양가"].convert_dtypes()


# 정렬
# res = df.sort_values(by="지역명")[:5]
# print(res)

res = df.sort_values("지역명")
res = df.sort_values("지역명", ascending=True)
res = df.sort_values("지역명", ascending=False)

print(res.head())
print(res.head(10))

res = df.sort_values(by="연도")
res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]

# print(res)
print(res.head())


# 컬럼 이름 출력

res = df["지역명"][:5]
res = df["지역명", "연도"]
res = df["지역명", "연도", "분양가"]
res = df["지역명", "면도", "분양가"][:7]

print(res)

print("========================")

# res = df.loc[:,"wlduraud", "연도", "분양가"][:5]
# res = df.loc[:][:5]
# res = df.loc[:][:]
res = df.iloc[1]

res = df.loc[:6, ["지역명", "연도"]][:3]
res = df.loc[6:, ["지역명", "연도"]][:7]
print(res)


res = df.loc[df["지역명"]=="서울", ["지역명", "면도", "분양가"]]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
res = df.loc[df["연도"] > 2020]

# 인덱스 지정 선택
df0 = df.copy()
print(df0)

print("===========================")

res = df.iloc[2]
res = df.iloc[2][2]
print(res)

# 인덱스 필터

res = df[df.index > 3500]
print(res)


df[df.연도 == 2023]
res = df[df.월 == 3]
print(res)
res = df[df.연도 == 2023] & df[(df.연도 == 2023)] & df[(df.지역명 == "서울")]
# res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
# print(res)


columns = list(df.columns)
print(columns + "컬럼")

df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + []
print(df)
print("===================")         
print(df1)


print("====================")
df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
print(df1)


# 복사

df2 = df1.copy()

# Nan 제거
res = df2.dropma(how="any")
res = df2.fillna(value ="text")
print(res)
res = df2.dropna(how="any", inplace=True)
print(df2)
print("----------------------------")

res = df2.dropna(how = "any", inplace=True)
print(res)
print(df2)


# res = pd.isna(df1)
# res = pd.isna(df)
# res = pd.isna(df0)
# res = pd.isna(df2)
# print(res)

# res = df["연도"].value_counts()
# res = df["지역명"].value_counts()
# res = df["월"].value_counts()
# res = df.월.value_counts()
# print(res)

res = df.groupby(["지역명", "연도", "월"]).sum()
# res = df.groupby(["지역명", "연도", "월"]).all()
print(res)


df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")








 """