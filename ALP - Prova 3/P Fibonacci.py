
def fibonacci(n, sequencia=None):
    if sequencia is None:
        sequencia = [0, 1]

    if n <= len(sequencia):
        return sequencia[:n]

    sequencia.append(sequencia[-1] + sequencia[-2])
    return fibonacci(n, sequencia)

value = int(input(""))
while value != 0:
    result = fibonacci(value)
    print(" ".join(map(str, result)))
    value = int(input(""))


