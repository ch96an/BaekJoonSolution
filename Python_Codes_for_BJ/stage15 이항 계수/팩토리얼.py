f = lambda x:1 if x==0 else x*f(x-1)
print(f(int(input())))