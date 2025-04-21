inicio, fim = map(int, input().split())

for numero in range(inicio, fim + 1):
    if numero <= 1:
        continue
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)