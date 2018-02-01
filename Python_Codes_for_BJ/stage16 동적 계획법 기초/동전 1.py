n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)])
lst = [[0]*(k+1)]*n+[[1]*(k+1)]
lst[0] = [1 if j%coin[0]==0 else 0 for j in range(0,k+1)]
for i in range(0, len(coin)):
	lst[i] = [sum([lst[i-1][j - (k * coin[i])] for k in range((j//coin[i])+1)]) for j in range(k+1)]
print(lst[n-1][k])