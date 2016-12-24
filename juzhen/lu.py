#coding: utf-8


def printmat(mat,n):
	for i in range(n):
		for j in range(n):
			print str(mat[i][j]),
			print " ",
		print "\n"	
def LU(A,n):
	L=[[0 for x in range(n)] for y in range(n)]
	U=[[0 for x in range(n)] for y in range(n)]

	for i in range(n,0,-1):
		for temp in range(n-i,n):#0--->i-1
			sumup=0
			for temp2 in range(n-i):
				sumup+=L[temp][temp2]*U[temp2][n-i]
			L[temp][n-i]=A[temp][n-i]-sumup

		for temp in range(n-i+1,n):
			sumup=0
			for temp2 in range(n-i):#0-->n-i-1
				sumup+=L[n-i][temp2]*U[temp2][temp]
			U[n-i][temp]=(A[n-i][temp]-sumup)/float(L[n-i][n-i])

	for i in range(n):
		U[i][i]=1
	#print "the L matrix is:"
	#printmat(L,3)	
	#print "the U matrix is:"
	#printmat(U,3)
	return (L,U)


def Solve(A,b,n):
	L=[[0 for x in range(n)] for y in range(n)]
	U=[[0 for x in range(n)] for y in range(n)]
	(L,U)=LU(A,n)
	Y=[0 for x in range(n)]
	X=[0 for x in range(n)]
	Y[0]=b[0]/float(L[0][0])
	for i in range(1,n):
		sumup=0
		for tmp in range(0,i):
			sumup+=L[i][tmp]*Y[tmp]
		Y[i]=(b[i]-sumup)/float(L[i][i])
	X[n-1]=Y[n-1]
	for i in range(n-2,-1,-1):
		sumup=0
		for tmp in range(i+1,n):
			sumup+=U[i][tmp]*X[tmp]
		X[i]=Y[i]-sumup
	return X


def main():
	A=[[16,4,8],[4,5,-4],[8,-4,22]]
	b=[-4,3,10]
	print u"A 矩阵为: "
	printmat(A,3)
	print u"b 矩阵为: "
	print b
	print u"LU 分解以后"
	print u"求得根为:"
	result=Solve(A,b,3)
	print result


if __name__ == '__main__':
	main()




	
		
	
