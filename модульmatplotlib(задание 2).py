import random
import numpy as np
import matplotlib.pyplot as plt

n=int(input("Введите количество элментов:"))
a=[]
for i in range(n):
    a1=random.randint(0,100)
    a.append(a1)
print(a)
mean=sum(a)/len(a)
print("Математическое ожидание:", mean)
otkl=(sum(((i-mean)**2 for i in a))/len(a))**0.5
print("Среднеквадратическое отклонение:",otkl)

k=0.5
b=4

f=np.array([k*x+b for x in range(n)])
y=f + np.random.normal(mean, otkl, n)
x=np.array(range(n))
mx=x.sum()/n
my=y.sum()/n
a2=np.dot(x.T, x)/n
a11=np.dot(x.T, y)/n

k1=(a11 - mx*my)/(a2 - mx**2)
b1=my - k1*mx

f1=np.array([k1*x+b1 for x in range(n)])

plt.plot(f1, c='green')
plt.scatter(x, y, s=2, c='red')
plt.grid()
plt.show()
