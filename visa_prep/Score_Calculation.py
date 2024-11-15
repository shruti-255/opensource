t = int(input())
for i in range(1, t+1):
    x, n = map(int, input().split())
    ans = (x//10)*n
    print(ans)
