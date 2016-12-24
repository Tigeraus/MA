#coding: utf-8


import math

def gs(matrix, arr):
    #xiaoyuan
    n = len(matrix)
    le = len(matrix[0])
    for i in range(n):
        for j in range(i+1,n):
            fac =  - matrix[j][i] / float(matrix[i][i])
            arr[j] = arr[j] + arr[i] * fac
            for k in range(n):
                matrix[j][k] = matrix[j][k] + matrix[i][k] * fac
    #qiu root
    rootl =[]
    for i in range(n-1,-1,-1):
        rsult=0
        tmp=0
        for r in range(len(rootl)):
            tmp = tmp + rootl[r] * matrix[i][n-1-r]
        rsult = (arr[i]-tmp)/float(matrix[i][i])
        rootl.append(rsult)
    rootl.reverse()

    return rootl


def main():
    m = [[1,1,1],[0,4,-1],[2,-2,1]]
    a = [6,5,1]
    print gs(m,a)

if __name__ == '__main__':
    main()
