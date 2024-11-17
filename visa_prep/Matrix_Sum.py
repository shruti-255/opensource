n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r_s = [0]*n
c_s = [0]*n
for i in range(n):
    for j in range(n):
        r_s[i] += arr[i][j]
        c_s[j] += arr[i][j]
r = [r_s[i] + c_s[i] for i in range(n)]
print(" ".join(map(str, r)))
