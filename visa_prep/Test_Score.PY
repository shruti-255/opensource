n, x, y = map(int, input().split())
ans = n*x
if(y%x==0 and y<=ans):
    print("YES")
else:
    print("NO")
