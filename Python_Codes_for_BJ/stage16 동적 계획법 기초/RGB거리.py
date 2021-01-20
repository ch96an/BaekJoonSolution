tmp = [0,0,0]
for _ in range(int(input())):
	a,b,c = map(int,input().split())
	tmp = [a+min(tmp[1:]),b+min(tmp[::2]),c+min(tmp[:2])]
print(min(tmp))