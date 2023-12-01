def organiza_palavra(palavra):
    return "".join(sorted(palavra.lower()))


def testa_anagramas(palavra1, palavra2):
    return organiza_palavra(palavra1) == organiza_palavra(palavra2)


while True:
    try:
        palavra1, palavra2 = input().split()
        resultado = testa_anagramas(palavra1, palavra2)
        print(resultado)
    except EOFError:
        break
