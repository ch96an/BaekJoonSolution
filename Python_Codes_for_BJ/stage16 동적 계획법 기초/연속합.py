f=lambda x,k:[max(x),max(x[1]+k,k)]
n,l,x=input(),list(map(int,input().split())),[0,0]
for c in l:x=f(x,c)
print(max(x) if max(x)!=0 else max(l))