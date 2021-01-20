dic = {(0,i):i for i in range(1,15)}
for x in range(1,15):
	for y in range(1,15):
		dic[(x,y)] = sum([dic[(x-1, k)] for k in range(1,y+1)])
for _ in range(int(input())):
	k, n = int(input()), int(input())
	print(dic[(k,n)])