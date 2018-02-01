n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
for i in range(n-1)[::-1]:
	for j in range(i+1):
		lst[i][j]+=max(lst[i+1][j],lst[i+1][j+1])
print(lst[0][0])