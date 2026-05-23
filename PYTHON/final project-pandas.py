with open("grades.csv","w",encoding="utf-8")as f:  
    f.write("name,major,age,score\n ali,math,22,17.5\n sara,physics,26,18\nnahid,biology,32,16 \n mahdi,math,27,18 \n masood,physics,40,17\n samane,biology,31,16")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("grades.csv")
print(df.head())
print(df.info())
print(df.describe())

print("average:",df["score"].mean())
print(df.groupby("major")["score"].mean())
print(df.groupby("major")["name"].count())
print(df[df["score"]<18])

df["status"] = ["pass" if s>=18 else "failed" for s in df["score"]]
print(df)


x = df["name"]
y = df["score"]

plt.figure(figsize=(5,5))
plt.title("scores of students",fontsize = 16, color = "red")
plt.xlabel("names")
plt.ylabel("scores")
plt.grid(True, linewidth=1.5)
plt.bar(x,y,color="blue")

print(plt.plot(x, y , marker = 'o', linestyle = "--"))
print(plt.show())







    