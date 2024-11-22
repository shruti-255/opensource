n = int(input())
arr = list(map(int, input().split()))
c_c = 0
m_c = 0
for i in range(0, n):
    if(arr[i] == 0):
        c_c = c_c+1
        m_c = max(c_c, m_c)
    else:
        c_c = 0
print(m_c)
