import sys
n = int(sys.stdin.readline())
ans,stack,j =[],[0],1
for i in range(n):
    s = int(sys.stdin.readline())
    if j <= s:
        while stack[-1] != s:
            stack.append(j)
            j += 1
            ans.append('+')
        ans.append('-')
        del stack[-1]
    else:
        if stack[-1]==s:
            ans.append('-')
            del stack[-1]        
        else:
            ans = 'NO'
            break
if ans == 'NO':
    print(ans)
else:
    for x in ans:print(x)