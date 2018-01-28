import sys
f1 = lambda lst,k:[x for x in lst if x%k!=0]
f2 = lambda n,lst,k,plst:plst+lst if n<k**2 else f2(n,f1(lst,lst[0]),lst[0],plst+[lst[0]])
f3 = lambda n:f2(n,list(range(2,n+1)),2,[])
f4 = lambda n:len([x for x in f3(2*n) if x>n])
print('\n'.join(map(lambda x: str(f4(int(x))),sys.stdin.read().split()[:-1])))