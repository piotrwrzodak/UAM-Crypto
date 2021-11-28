def pow_exp(a, x, n):
    m = str(bin(x)[2:])
    p = 1
    for c in m:
        x = int(c)
        if x == 0:
            p = p * p % n
        elif x == 1:
            p = p * p * a % n
    return p


# print(pow_exp(3, 2**30, 2**100 - 1))
# print(pow_exp(10, 3 ** 39 + 1, 2**62 + 10))
