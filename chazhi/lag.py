#coding: utf-8

import math

def Lagrange(x,xlist,ylist):
    y=0
    n=len(ylist)
    for i in range(n):
        t = 1
        for j in range(n):
            if i!=j:
                t = t*(x-xlist[j])/(xlist[i]-xlist[j])
                #print 't=',t
        y = y+t*ylist[i]
    return y





def main():
    xl = [1,2,3,4,5,6,7,8]
    yl = [1,3,2,4,6,2,8,20]
    print Lagrange(10,xl,yl)
    lagrange(10,xl,yl,8)

if __name__ == '__main__':
    main()