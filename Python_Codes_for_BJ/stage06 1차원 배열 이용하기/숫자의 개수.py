x = lambda:int(input())
s = str(x()*x()*x())
for i in range(10):
	print(s.count(str(i)))