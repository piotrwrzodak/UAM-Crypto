from piotr_wrzodak_16_2 import pow_exp


def task5(b, p):
    result = pow_exp(b, (p - 1) // 2, p)
    if result == 1:
        return pow_exp(b, (p + 1)//4, p)
    else:
        return 'b nie jest reszta kwadratowa'


# print(task5(2, 2**(201) - 313))
# print(task5(3, 2**(201) - 313))
# print(task5(11, 2**33 - 9))
# print(task5(10, 2**33 - 9))
