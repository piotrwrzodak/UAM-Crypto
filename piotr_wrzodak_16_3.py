import random


def task3(n):
    for i in range(5):
        a = random.randrange(2, 1000)
        result = pow(a, n - 1, n)
        # print(n, a, result)
        if result != 1:
            break

    if result != 1:
        return 'n jest liczba zlozona'
    else:
        return 'n jest prawdopodobnie liczba pierwsza'


# print(task3(2**201 - 313))
# print(task3(2**201 - 323))
# print(task3(2**33 - 9))
# print(task3(2**(33) - 21))
