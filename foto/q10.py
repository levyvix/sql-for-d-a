def find_substrings(k, word):
    if k == 0:
        return []

    substrings = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substring = word[i:j]
            unique_chars = set(substring)
            if all(substring.count(char) == k for char in unique_chars):
                substrings.add(substring)
    return substrings


def main():
    while True:
        k, word = input().split()
        k = int(k)
        if k == 0:
            break
        substrings = find_substrings(k, word)
        print(" ".join(sorted(substrings)) if substrings else "NONE")


if __name__ == "__main__":
    main()
