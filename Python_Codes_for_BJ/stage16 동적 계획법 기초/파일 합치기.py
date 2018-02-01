import sys;input=sys.stdin.readline
for _ in range(int(input())):
	n,lst,s = int(input()),list(map(int,input().split())),[0]
	for i in range(n):s.append(s[-1]+lst[i])
	memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
	memo_k = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(n):memo_k[i][i+1]=i+1
	for d in range(2,n+1):
		for i in range(n-d+1):
			j = i+d
			memo[i][j] = float('inf')
			for k in range(memo_k[i][j-1],memo_k[i+1][j]+1):
				tmp = memo[i][k]+memo[k][j]+s[j]-s[i]
				if tmp < memo[i][j]:
					memo[i][j] = tmp
					memo_k[i][j] = k
	print(memo[0][n])