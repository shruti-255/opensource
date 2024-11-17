t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    res = x//10
    print(int(res*n))
