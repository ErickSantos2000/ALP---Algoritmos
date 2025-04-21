senha = input()

if len(senha) > 8 and senha.count('!') + senha.count('?') + senha.count('.') > 0 and sum(1 for char in senha if char.isdigit()) >= 3:
    print("OK")
else:
    print("FAIL")
