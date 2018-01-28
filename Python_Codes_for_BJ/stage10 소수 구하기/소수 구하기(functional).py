f1 = lambda lst,k:[x for x in lst if x%k!=0]
f2 = lambda n,lst,k,plst:plst+lst if n<k**2 else f2(n,f1(lst,lst[0]),lst[0],plst+[lst[0]])
f3 = lambda n:f2(n,list(range(2,n+1)),2,[])
M, N = map(int,input().split())
lst = [x for x in f3(N) if x >= M]
for x in lst:print(x)