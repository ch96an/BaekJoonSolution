#m,n = map(int,input().split())
f1 = lambda lst,k:[x for x in lst if x%k!=0]
f2 = lambda n,lst,k:lst if k**2>n else f2(n,f1(lst,k),k+1)
f3 = lambda n:f2(n,list(range(2,n+1)),2)
print(f3(100000))