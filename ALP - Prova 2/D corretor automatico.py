corretor = []
while True:
    linha = input().strip()
    if linha == '':
        break 
    elif linha == 'AUTOJUDGE':
        for arquivo in corretor:
            if arquivo [1]:
                print(arquivo[0],'C')
            else:
                print(arquivo[0],'W')
                arquivo[1] = True
              
        print('=')
    else:
        corretor.append([linha, False])