n, m = map(int, input().split())
arr = list(map(int, input().split()))
num1 = num2 = 0
for i in arr:
    if(i%m==0):
        num1 += i
    else:
        num2 += i
print(num1 - num2)
