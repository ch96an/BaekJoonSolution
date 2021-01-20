import sys; ssr = sys.stdin.readline
for _ in range(int(ssr())):
	n,k = map(int,ssr().split())
	cost = [0]+list(map(int,ssr().split()))
	time = [0 for _ in range(n+1)]
	edge = [[] for _ in range(n+1)]
	for _ in range(k):
		i,j = map(int,ssr().split())
		edge[j].append(i)
	target = int(ssr())
	visited = []
	stack = [target]
	while stack:
		current = stack.pop()
		search = [x for x in edge[current] if x not in visited]
		if search:
			stack.append(current)
			stack.append(search[0])
		else:
			visited.append(current)
	for v in visited:
		time[v] = max([time[x] for x in edge[v]],default=0)+cost[v]
	print(time[target])