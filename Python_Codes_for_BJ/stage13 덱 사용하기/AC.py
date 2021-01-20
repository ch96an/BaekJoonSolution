mysplit = lambda x:x.split(',') if x else []
reader = lambda:list(map(int,mysplit(input()[1:-1])))
printer = lambda x:print('['+','.join(map(str,x))+']')
def counter(s):
	X,tmp = [0,0],0
	for c in s:
		if c=='R':tmp=1-tmp;continue
		X[tmp]+=1
	return X,tmp

def apply(count,lst):
	X,tmp = count
	a,b = X
	if len(lst)<sum(X):print('error')
	elif tmp:printer(lst[a:-b][::-1]) if b else printer(lst[a:][::-1])
	else:printer(lst[a:-b]) if b else printer(lst[a:])

for _ in range(int(input())):
	p,n,lst=input(),input(),reader()
	apply(counter(p),lst)