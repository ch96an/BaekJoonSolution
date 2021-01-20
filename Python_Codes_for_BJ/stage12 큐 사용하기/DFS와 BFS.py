N, M, S = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for i in range(M):
	i, j = map(int, input().split())
	graph[i] += [j]
	graph[j] += [i]
for i in range(1, N+1):
	graph[i] = sorted(graph[i])

def dfs(graph, node, lst = [], dic = {i:True for i in range(1, N+1)}):
	if dic[node]:
		lst.append(node)
		dic[node] = False
		for adjacent in graph[node]:
			dfs(graph, adjacent, lst, dic)
	return lst

def bfs(graph, start, lst = [], dic = {i:True for i in range(1, N+1)}):
	queue = [start]
	while queue:
		tmp = queue.pop(0)
		if dic[tmp]:
			dic[tmp] = False
			lst.append(tmp)
			queue += [x for x in graph[tmp] if dic[x]]
	return lst

print(" ".join(map(str, dfs(graph, S))))
print(" ".join(map(str, bfs(graph, S))))