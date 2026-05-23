import numpy as np
np.random.seed(1234)
a = np.random.randint(0,20,size=100)
print(a)
print("avg:",a.mean())
print("minimum:",a.min())
print("maximum:",a.max())
print("standard_devision:",a.std())
passed = a[a>=10]
print("number of passed:",len(passed),"from",len(a))
print("percent of passed:",len(passed)/len(a)*100,"%")
excellent = a[a>17]
print("excellent_grades:", excellent)
print("sorted grades:\n",np.sort(a))





