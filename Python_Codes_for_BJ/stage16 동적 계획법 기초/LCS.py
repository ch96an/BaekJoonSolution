s0,s1=input(),input()
n0,n1=len(s0),len(s1)
dic={(i,j):0 for i in range(-1,n0) for j in range(-1,n1)}
for i in range(0,n0):
	for j in range(0,n1):
		dic[(i,j)]=dic[(i-1,j-1)]+1 if s0[i]==s1[j] else max(dic[(i-1,j)],dic[(i,j-1)])
print(dic[(n0-1,n1-1)])