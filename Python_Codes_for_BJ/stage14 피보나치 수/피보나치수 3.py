a, dic = [0,1], {'0':[[1,0],[0,1]], '1':[[1,1],[1,0]]}
mm=lambda x,y:[[sum([x[i][k]*y[k][j] for k in a])%1000000 for i in a] for j in a]
sq=lambda x:mm(x,x)
fib = lambda s:dic[s] if int(s) in a else mm(sq(fib(s[:-1])),dic[s[-1]])
print(fib(bin(int(input()))[2:])[0][1])