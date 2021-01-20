import sys
counter = [0 for _ in range(10001)]
for i in range(int(sys.stdin.readline())):
	counter[int(sys.stdin.readline())] += 1
for i in range(1,10001):
	for j in range(counter[i]):
		print(i)