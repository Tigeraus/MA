#coding: utf-8


import math



def get_xishulist(xlist,ylist):
    xishulist=[]
    for i in range(len(xlist)):
        if i==0:
            xishulist.append(ylist[0])
        else:
            fx = 0
            num=0#求和总数
            num=i+1
            for k in range(num):
                tmp = 1
                for j in range(num):
                    if k != j:
                        tmp = tmp * (xlist[k] - xlist[j])
                    else:
                        continue
                fx = fx + float(ylist[k])/tmp
            print fx
            xishulist.append(fx)
    return xishulist


def generate_func(xishulist,xlist):
    def f(x):
        result=0
        for i in range(len(xishulist)):
            tmp = xishulist[i]
            for j in range(i):
                tmp= tmp * (x - xlist[j])

            result = result + tmp
        
        return result
    return f


def main():
    xl=[0.40,0.55,0.65,0.80,0.90,1.05]
    yl=[0.41075,0.57815,0.69675,0.88811,1.02652,1.25382]
    if len(xl) == len(yl):
        xishul = get_xishulist(xl,yl)
        func = generate_func(xishul,xl)
        print func(0.596)
    else:
        print u'长度不一致'


if __name__ == '__main__':
    main()