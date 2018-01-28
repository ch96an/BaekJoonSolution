_isprime = lambda x,k: True if x<k**2 else False if x%k==0 else _isprime(x,k+1)
isprime = lambda x: _isprime(x,2) if x>=2 else False
lst = [x for x in range(int(input()),int(input())+1) if isprime(x)]
print(str(sum(lst))+'\n'+str(lst[0]) if lst else -1)