input()
_isprime = lambda x,k: True if x<k**2 else False if x%k==0 else _isprime(x,k+1)
isprime = lambda x: _isprime(x,2) if x>=2 else False
print(len([0 for x in list(map(int,input().split())) if isprime(x)]))