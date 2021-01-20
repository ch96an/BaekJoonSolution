import sys
#x = list(map(int,sys.stdin.read().split()[1:]))
x = [4,2,3,1]

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

def insertionSort(x):
	y=[]
	for i in range(len(x)):
		y = mergeList(y,[x[i]])
	return y

for i in insertionSort(x):
	print(i)