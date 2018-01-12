base = ["  *  "," * * ","*****"]
double = lambda x : x+" "+x
spacer = lambda x, k: "   "*k + x + "   "*k
k, n = 1, int(input())
while n > 3*k:
	base = list(map(lambda x:spacer(x,k), base))+list(map(double,base))
	k *= 2
print("\n".join(base))