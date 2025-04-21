def ark(m,n,p):
    if p == 0:
        return m + n
    elif p == 1:
        return m*n
    elif p == 2:
        return m**n
    elif p > 2 and n == 0:
        return m
    elif n > 0 and p > 0:
        return ark(m, ark(m ,n -1 ,p),p - 1 )
    
while True:
    m ,n ,p = map(int, input().split())
    print(ark(m, n, p))
    if m == 0 and n == 0 and p == 0:
        break


