while True:
    entrada = input()
    if entrada == "_FIM_":
        break
    
    palavras = entrada.split()
    contador = 0
    
    for palavra in palavras:
        if len(palavra) > 2:
            contador += 1
    
    print(contador)


