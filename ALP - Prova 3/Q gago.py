def generate_sequence(s):
    return [] if not s else generate_sequence(s[:-1]) + [s]

entrada = input()
for item in generate_sequence(entrada):
    print(item)

