#coding: utf-8

import math


def int_NC(xlrange,ylist):
    sum = xlrange[1]-xlrange[0]
    n = len(ylist)

    if n == 2:
        xishulist=[0.5,0.5]
    elif n == 3:
        xishulist=[1.0/6.0,2.0/3.0,1.0/6.0]
    elif n == 4:
        xishulist=[1.0/8.0,3.0/8.0,3.0/8.0,1.0/8.0]
    elif n == 5:
        xishulist=[7.0/90, 16.0/45, 2.0/15, 16.0/45, 7.0/90]
    elif n == 6:
        xishulist=[19.0/288, 25.0/96, 25.0/144, 25.0/144, 25.0/96, 19.0/288]
    elif n == 7:
        xishulist=[41.0/840, 9.0/35, 9.0/280, 34.0/105, 9.0/280, 9.0/35, 41.0/840]
    elif n == 8:
        pass
    elif n == 9:
        pass
    else:
        print 'err'
        return 0
    for i in range(len(xishulist)):
        sum = sum + xishulist[i]*ylist[i]
    return sum



def main():
    xr = [0,1]
    ylist = [1,2,4,5,7,-3]
    print int_NC(xr,ylist)
    pass

if __name__ == '__main__':
    main()