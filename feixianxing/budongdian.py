#coding: utf-8

import math


def phi(x):
    return math.pow(x+1,1.0/3)


def stopp(func,errorange,initroot):
    nextroot = func(initroot)
    if abs(nextroot-initroot) < errorange:
        return nextroot
    else:
        return stopp(func,errorange,nextroot)


def stopp_Atk(func,errorange,initroot):
    nextroot1 = func(initroot)
    nextroot2 = func(nextroot1)
    nextroot = initroot - math.pow(nextroot1-initroot,2) / float(nextroot2 - 2 * nextroot1 + initroot)
    if abs(nextroot-initroot) < errorange:
        return nextroot
    else:
        return stopp(func,errorange,nextroot)


def stopp_Stf(func,errorange,initroot):
    xk = initroot
    yk = func(xk)
    zk = func(yk)
    nextroot = xk - math.pow(yk - zk,2) / float(zk - 2 * yk + xk)
    if abs(nextroot-initroot) < errorange:
        return nextroot
    else:
        return stopp(func,errorange,nextroot)


def main():
    er = math.pow(10,-7)
    print stopp(phi,er,50)
    print stopp_Atk(phi,er,50)
    print stopp_Stf(phi,er,50)


if __name__ == '__main__':
    main()