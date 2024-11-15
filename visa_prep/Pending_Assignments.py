x, y, z = map(int, input().split())
time_needed = x*y
time_given = z*24*60
if(time_needed<=time_given):
    print("YES")
else:
    print("NO")
