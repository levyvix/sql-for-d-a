def calcular_histograma(N, M, P, imagem):
    histograma = [0] * P

    for linha in imagem:
        for pixel in linha:
            histograma[pixel] += 1

    total_pixels = N * M
    histograma_probabilidades = [x / total_pixels for x in histograma]

    return histograma_probabilidades


while True:
    N, M, P = map(int, input().split())
    if N == -1:
        break

    imagem = []
    for _ in range(N):
        linha = list(map(int, input().split()))
        imagem.append(linha)

    histograma_probabilidades = calcular_histograma(N, M, P, imagem)
    output = " ".join([f"{prob:.2f}" for prob in histograma_probabilidades])
    print(output)
