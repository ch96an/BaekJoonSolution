C=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=input()
for i in C:
	s = s.replace(i,"_")
print(len(s))