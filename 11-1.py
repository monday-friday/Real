import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"


df = pd.read_csv(target)

df.name == "김영수"

print(df.name == "김영수")
















