alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x, s = [0]*26, input().upper()
for i in range(26):
	x[i] = s.count(alphabet[i])
if x.count(max(x))>1:
	print("?")
else:
	print(alphabet[x.index(max(x))])