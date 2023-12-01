def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def calcular_soma_fatoriais(valores):
    return sum(fatorial(x) for x in valores)


while True:
    try:
        entrada = input()
        if not entrada:
            break
        valores = list(map(int, entrada.split()))
        soma_fatoriais = calcular_soma_fatoriais(valores)
        print(soma_fatoriais)
    except EOFError:
        break
