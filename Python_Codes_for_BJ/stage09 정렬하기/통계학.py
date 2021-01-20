import sys
from collections import Counter
x = list(map(int, sys.stdin.read().split()))[1:]
x.sort()
print(round(sum(x)/len(x)))
print(x[(len(x)-1)//2])
c = Counter(x)
tmp, lst = c.most_common(1)[0][1], []
for i in range(-4000,4001):
	if c[i]==tmp:lst.append(i)
lst.sort()
print(lst[0] if len(lst)==1 else lst[1])
print(x[-1]-x[0])