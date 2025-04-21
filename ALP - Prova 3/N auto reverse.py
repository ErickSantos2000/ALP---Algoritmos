
def auto_reverso(string):
    if not string:
        return
    else:
        print(string[-1], end="")
        auto_reverso(string[:-1])


entrada = input()

auto_reverso(entrada)
print()
