def eh_divisivel(N):
    produto = 1
    soma = 0

    for i in range(1, N + 1):
        produto *= i
        soma += i

    if produto % soma == 0:
        return "OK"
    else:
        return "NOTOK"


n = int(input())
for _ in range(n):
    N = int(input())
    resultado = eh_divisivel(N)
    print(resultado)
