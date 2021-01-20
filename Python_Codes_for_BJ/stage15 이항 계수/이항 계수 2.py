n,k=map(int,input().split())
tmp=1
for i in range(1,n+1):tmp*=i
for i in range(1,k+1):tmp//=i
for i in range(1,n-k+1):tmp//=i
print(tmp%10007)