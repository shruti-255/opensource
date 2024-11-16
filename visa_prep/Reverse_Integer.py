def r_i(n):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if n<0:
        sign = -1
    else:
        sign = 1
    r_n = int(str(abs(n))[::-1])*sign
    if r_n < INT_MIN or r_n > INT_MAX:
        return 0
    return r_n
n = int(input())
print(r_i(n))
