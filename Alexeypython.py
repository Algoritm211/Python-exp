import math
'''f = open('input.txt', 'r')
w = open('output.txt', 'w')
k=[]
for i in f.read().split():
   k.append(int(i))
f.close()
w.close()'''
####################################
import array
import random
import datetime

'''time.sleep(0.5)
#n=(input("stroki "))
#m=(input("stolbtsy "))
while True:
    try:
        o = (input("Введите количество строк "))
        l = (input("Введите количество столбцов "))
        if o.isalpha() or int(o) < 0 or l.isalpha() or int(l) < 0 :
            raise  Exception
        break

    except Exception:
        print("Женя, ну вот зачем ты так, а, что я тебе сделал? Почему ты так жесток?")


n=int(o)
m=int(l)
a=[]
for i in range(n):
    b=[]
    for j in range (m):
        b.append(random.randint (10,20))
    a.append(b)
sum1=0
sum2=0
for i in range(n):
    for j in range (m):
        if(a[i][j]>15):
            sum1+=a[i][j]
        elif(a[i][j]<15):
            sum2+=a[i][j]
print(sum1)
print(sum2)
for i in a:
     print(*i)
for i in range(n):
    for j in range (m):
        if(i==j):
            a[i][j]=0
        elif(i>j):
            a[i][j]=sum1
        elif(i<j):
            a[i][j]=sum2


for i in a:
     print(*i)'''
#############################################
import numpy as np
'''
def square(a):
    b=[]#сторона
    b.append(a)
    p=4*a
    b.append(p)
    s=a*a
    b.append(s)
    d=a*math.sqrt(2)
    b.append(d)
    c=tuple(b)
    print(c)
def bank(a,s):
    for i in range(s):
        a=a+a*0.1
    print(a)
'''
#a=int(input("Сторона "))
#square(a)
#a=int(input("sum "))
#s=int(input("years "))
#bank(a,s)
#################################

'''a=int(input())
b=int(input())
while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
nod=a+b
print(nod)
#################################
import io
candidates = {}
voices = 0

with io.open("input.txt", "r", encoding="utf-8") as inf:
    for name in map(str.strip, inf):
        candidates[name] = candidates.get(name, 0) + 1
        voices += 1


candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

with io.open("output.txt", "w", encoding="utf-8") as out:
    percent = candidates[0][1] / voices * 100
    if percent > 50:
        print(candidates[0][0], file=out)
    else:
        for name, _ in candidates[:2]:
            print(name, file=out)
print(voices)
out.close()
inf.close()
'''
################################
print(datetime.datetime.now().strftime('%d-%m'))
