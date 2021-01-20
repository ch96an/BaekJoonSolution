n, m = map(int, input().split())
row = [list(map(int, input().split())) for i in range(n)]
route_memo = {(n-1,m-1):1}
vector = [[1,0],[-1,0],[0,1],[0,-1]]
def route(a,b):
	if (a,b) in route_memo.keys():
		return route_memo[(a,b)]
	tmp = 0
	for v in vector:
		a1, b1 = a + v[0], b + v[1]
		tmp += route(a1, b1) if 0<=a1<n and 0<=b1<m and row[a1][b1]<row[a][b] else 0
	route_memo[(a,b)] = tmp
	return tmp
print(route(0,0))