"""
this code do not pass
use different language or use built-in function(see 'easy answer')
"""
import sys
lst = list(map(int,sys.stdin.read().split()))[1:]

def mergeList(L,R):
	y=[]
	while L and R:
		if L[0]<R[0]:
			y.append(L[0])
			L = L[1:]
		else:
			y.append(R[0])
			R = R[1:]
	y = y+R+L
	return y

def mergeSort(x):
	if len(x)>1:
		M = len(x)//2
		L = mergeSort(x[:M])
		R = mergeSort(x[M:])
		y = mergeList(L,R)
		return y
	else:
		return x

for i in mergeSort(lst):
	print(i)