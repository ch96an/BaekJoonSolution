import math
f = lambda n : int((-1+math.sqrt(8*(n-1)+1))/2)+2
g = lambda n : int((n-2)*(n-1)/2)
def h(n):
	if f(n)%2 == 0:
		k = n - g(f(n))
		print('{0}/{1}'.format(f(n)-k,k))
	else:
		k = n - g(f(n))
		print('{1}/{0}'.format(f(n)-k,k))
h(int(input()))