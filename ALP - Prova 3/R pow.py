def pow(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n - 1)


a, n = map(int, input().split())


resultado = pow(a, n)
print(resultado)


