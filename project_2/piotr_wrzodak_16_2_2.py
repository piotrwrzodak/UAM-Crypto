import random

from project_1.piotr_wrzodak_16_1_5 import task5
from project_2.piotr_wrzodak_16_2_1 import generate_elliptic_curve


def find_point(a, b, p):
    x = random.randrange(p - 1)
    print("x:", x)

    y = task5(pow(x, 3) + a * x + b, p)
    while not y[0]:
        x = random.randrange(p - 1)
        print("x:", x)
        y = task5(pow(x, 3) + a * x + b, p)
    print(y)

    left = y[1]**2 % p
    right = (pow(x, 3) + a * x + b) % p
    print(left == right, left, right)

    return [x, y[1]]


if __name__ == "__main__":
    v1, v2, v3 = generate_elliptic_curve()
    print(find_point(v1, v2, v3))

    print("\n")
    v1, v2, v3 = generate_elliptic_curve()
    print(find_point(v1, v2, v3))
