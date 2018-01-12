import sys
x = list(map(int,sys.stdin.read().split()[1:]))

def bubbleSort(x):
	for i in range(len(x)):
		for j in range(len(x)-1):
			if x[j]>x[j+1]:
				(x[j],x[j+1])=(x[j+1],x[j])
	return x

for i in bubbleSort(x):
	print(i)