from project_1.piotr_wrzodak_16_2 import pow_exp


def task4(b, p):
    result = pow_exp(b, (p - 1)//2, p)
    if result == 1:
        return 'b jest reszta kwadratowa'
    else:
        return 'b nie jest reszta kwadratowa'


# print(task4(2, 2**(201) - 313))
# print(task4(3, 2**(201) - 313))
# print(task4(11, 2**33 - 9))
# print(task4(10, 2**33 - 9))
