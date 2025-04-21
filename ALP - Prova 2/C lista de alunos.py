lista = []
presenca = input()
while True:
    lista.append(presenca)
    nome = input()
    if nome in "FIM":
        break
    if nome in presenca:
        print(f"{nome} PRESENTE")
        
    else:
        print(f"{nome} AUSENTE")