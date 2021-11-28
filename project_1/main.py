from project_1.piotr_wrzodak_16_1 import euclidean_algorithm
from project_1.piotr_wrzodak_16_2 import pow_exp
from project_1.piotr_wrzodak_16_3 import task3
from project_1.piotr_wrzodak_16_4 import task4
from project_1.piotr_wrzodak_16_5 import task5


def project_1():
    print("1.")
    # liczba, mod => odwrotność
    print(euclidean_algorithm(3, 2 ** 30 - 5))
    print(euclidean_algorithm(100, 54321))
    print("\n2.")
    print(pow_exp(3, 2 ** 30, 2 ** 100 - 1))
    print(pow_exp(10, 3 ** 39 + 1, 2 ** 62 + 10))
    print("\n3.")
    print(task3(2 ** 201 - 313))
    print(task3(2 ** 201 - 323))
    print(task3(2 ** 33 - 9))
    print(task3(2 ** (33) - 21))
    print("\n4.")
    print(task4(2, 2 ** (201) - 313))
    print(task4(3, 2 ** (201) - 313))
    print(task4(11, 2 ** 33 - 9))
    print(task4(10, 2 ** 33 - 9))
    print("\n5.")
    print(task5(2, 2 ** (201) - 313))
    print(task5(3, 2 ** (201) - 313))
    print(task5(11, 2 ** 33 - 9))
    print(task5(10, 2 ** 33 - 9))


if __name__ == '__main__':
    project_1()

