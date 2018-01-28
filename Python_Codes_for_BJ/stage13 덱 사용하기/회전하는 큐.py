N, M = map(int, input().split())
lst = list(map(int, input().split()))
queue = list(range(1, N+1))
tmp = 0
for x in lst:
	k = queue.index(x)
	tmp += min(k, len(queue)-k)
	queue = queue[k+1:]+queue[:k]
print(tmp)