lista =["Pedro", "Adnilton", "Alcymara", "Jose", "Allan", "Bastiao", "Ana Carolina", "Ana Julia", "Severino", "Anderson", "Andre"]
while lista: 
    try:

        n = int(input(''))
        if n <= len(lista) :
            print(lista.pop(n))
        elif len(lista) <=  n :
            print('**ALEM DO ULTIMO**')
    except ValueError:
            break
    
   		