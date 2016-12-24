#coding=utf-8

def lagrange(x,xt,yt,n):
    y = 0
    for i in range(n):
        t = 1
        for j in range(n):
            if i!=j:
                t = t*(x-xt[j])/(xt[i]-xt[j])
        y = y+t*yt[i]
    print("结果为：%f" %y)

xt = [1,2,3,4,5,6,7,8]
yt = [1,3,2,4,6,2,8,20]
n=8
x=10
lagrange(x,xt,yt,n)