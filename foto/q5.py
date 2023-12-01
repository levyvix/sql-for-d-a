def count_characters(text):
    character_count = {}
    text = text.replace(" ", "").replace("\n", "")

    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    # Ordenar o dicionário por contagem (decrescente) e, em caso de empate, por caractere (crescente)
    sorted_characters = sorted(
        character_count.items(), key=lambda item: (-item[1], item[0])
    )

    for char, count in sorted_characters:
        print(f"{char} {count}")

    print("-1")


# Ler o número de testes
num_tests = int(input())


text = [input() for _ in range(num_tests)]
for t in text:
    count_characters(t)
