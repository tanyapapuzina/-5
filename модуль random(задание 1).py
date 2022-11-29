from random import randint
print('Введите количесвто элементов в списке:')
n = int(input())
b = []
for i in range(n):
    b.append(randint(0,1))
print(b)
for i in range(1,n+1):
    c = 0
    for j in range(0, n - i+1):
        if sum(b[j:j+i])==0:
            c=c+1
    c=c/(n-i+1)
    p=0
    for j in range(0, n - i+1):
        if sum(b[j:j+i])==i:
            p=p+1
    p=p/(n-i+1)
    if p==c==0:
        break
    print("Вероятность", i*"0", ":", c)
    print("Вероятность", i*"1", ":", p)
