cycle = lambda x: (x%10)*10 + (x%10+x//10)%10
repeat = lambda n, i, x: i if n == x else repeat(n, i+1, cycle(x))
repeat2 = lambda n: repeat(n,1,cycle(n))
print(repeat2(int(input())))