def calcular_eqm(valores):
    n = len(valores)
    media = sum(valores) / n
    eqm = sum((valor - media) ** 2 for valor in valores) / n
    return round(eqm, 2)


def main():
    num_casos = int(input())

    for _ in range(num_casos):
        valores = list(map(float, input().split()))

        eqm = calcular_eqm(valores)
        print(eqm)


if __name__ == "__main__":
    main()
