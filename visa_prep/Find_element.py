n = int(input())
arr = list(map(int, input().split()))
x = int(input())
flag = False
for i in range(n):
    if(arr[i]==x):
        print(i)
        flag = True
        break
if(flag==False):
    print(-1)
