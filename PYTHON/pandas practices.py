with open("students.csv","w",encoding = "utf-8")as f:
    f.write("name,age,score\n ali,22,18.5 \n saeed,31,20 \n samane,32,17")
    
import pandas as pd
df = pd.read_csv("students.csv")
print(df.head())



print(df.iloc[1])

df["status"] = ["excellent"if s>18 else "normal" for s in df["score"]] 
print(df)

print(df.tail())
print(df.info())
print(df.describe())
print(df[df["score"]>18])

print(df[["score","age"]])

print(df["name"]) 