numeros_impares = []
while True:
    try:
        entrada = input()
        if entrada == 'FIM':
            break
        numero = int(entrada)
        if numero % 2 == 1 and numero not in numeros_impares:
            numeros_impares.append(numero)
    except ValueError:

        pass

numeros_impares.reverse()
print(' '.join(map(str, numeros_impares)))