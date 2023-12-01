def myjoin(*paths):
    # new_paths = []
    new_paths = list(map(lambda x: x.replace("/", "").replace("\\", ""), paths))

    return "/".join(new_paths)


while True:
    n = int(input())
    if n == -1:
        break
    paths = []
    for _ in range(n):
        path = input()
        paths.append(path)

    concatenated_path = myjoin(*paths)
    print(concatenated_path)
