def euclidean_algorithm(x, y):
    a = [1, 0, x]
    b = [0, 1, y]

    while a[2] % b[2] != 0 and b[2] % a[2] != 0:
        # print(a, b)
        if a[2] > b[2]:
            q = a[2] // b[2]
            for i in range(0, 3):
                a[i] = a[i] - q * b[i]
        else:
            q = b[2] // a[2]
            for i in range(0, 3):
                b[i] = b[i] - q * a[i]
    # print('r',a, b)
    if a[2] > b[2]:
        return b[0]
    else:
        return a[0]


# print(euclidean_algorithm(3, 2**30 - 5))
# print(euclidean_algorithm(100, 54321))
