import sys
sys.setrecursionlimit(10**7)
def f(n, i, m, bj, bm, d):
	if i == n: return "{0}/{1}".format(bj,bm)
	if d == 0 and bj == m:
		return f(n,i+1,m+1,bj+1,bm,1)
	if d == 0 and bj <= m:
		return f(n,i+1,m,bj+1,bm-1,0)
	if d == 1 and bj == 1:
		return f(n,i+1,m+1,bj,bm+1,0)
	if d == 1 and bj >= 1:
		return f(n,i+1,m,bj-1,bm+1,1)
print(f(int(input()),1,1,1,1,1))