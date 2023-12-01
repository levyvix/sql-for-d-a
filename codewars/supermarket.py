number = 50123

number_list = [
    n + "0" * len(str(number)[i + 1 :]) for i, n in enumerate(str(number)) if n != "0"
]
print(" + ".join(number_list))
