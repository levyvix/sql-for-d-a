def calcular_fatores_em_comum(a, b):
    fatores_comuns = 0
    min_valor = min(a, b)

    for i in range(1, min_valor + 1):
        if a % i == 0 and b % i == 0:
            fatores_comuns += 1

    return fatores_comuns


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    fatores = calcular_fatores_em_comum(a, b)

    if fatores > 0 and fatores <= 10**5:
        print(fatores)
    else:
        print(0)
