l=[1,1,1,2,2]
for i in range(5,100):l+=[l[-5]+l[-1]]
for i in range(int(input())):print(l[int(input())-1])