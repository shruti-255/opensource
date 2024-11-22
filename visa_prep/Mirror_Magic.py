n = int(input())
arr = []
for i in range(n):
    r = list(map(int, input().split()))
    arr.append(r)
for r in arr:
    print(*r[::-1])
    
