# coding: utf-8
import math

def rKN(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x






def rK4(xy,func,h):
    x = xy[0]
    y = xy[1]
    k1 = func(x,y)
    k2 = func(x + 0.5 * h, y + 0.5 * h * k1)
    k3 = func(x + 0.5 * h, y + 0.5 * h * k2)
    k4 = func(x + h, y + h * k3)
    xp = x + h
    yp = y + (h/6.0) * (k1 + 2 * (k2 + k3) + k4)
    return (xp,yp)



def tryf(x,y):
    return math.pow(x,2) + 100 * math.pow(y,2)

def tryf1(x,y):
    return x + y

def tryf2(x,y):
    return y - float(2 * x)/y



def fa1(x):
    return 0.9*(1 - x[1]*x[1])*x[0] - x[1] + math.sin(x[2])

def fb1(x):
    return x[0]

def fc1(x):
    return 0.5

def VDP1():
    f = [fa1,fb1,fc1]
    x = [1, 1, 0]
    hs = 0.05
    for i in range(200):
        x = rKN(x, f, 3, hs)
    




def main():
    h = 0.001
    initxy = (0,1)
    for i in range(1000):
        xy  = rK4(initxy,tryf1,h)
        print xy[1]
        initxy = xy


if __name__ == '__main__':
    main()