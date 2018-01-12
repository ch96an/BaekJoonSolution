days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
a, b = map(int, input().split(' '))
print(days[(sum(dayOfMonth[0:a-1])+b-1)%7])