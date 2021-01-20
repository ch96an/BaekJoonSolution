n = int(input())

tools = [lambda x, k: "   "*k + x + "   "*k, lambda x, k: x+" "+x]
base = ["  *  "," * * ","*****"]
logsearch = lambda n, k, i:i if n<=k else logsearch(n,2*k,i+1)
normalizer = lambda bs, l: list(map(int,"0"*(l-len(bs))+bs))
applier = lambda bs, l, x, k: x if k==l else applier(bs,l,tools[bs[k]](x,2**k),k+1)
ith_Line = lambda i, length:applier(normalizer(bin(i//3)[2:],length)[::-1],length,base[i%3],0)

length = logsearch(n,3,0)

for i in range(n):
	print(ith_Line(i,length))