from project_2.piotr_wrzodak_16_2_1 import generate_elliptic_curve
from project_2.piotr_wrzodak_16_2_2 import find_point


def project_2():
    print("1.")
    a, b, c = generate_elliptic_curve()
    print(a, b, c)
    d, e, f = generate_elliptic_curve()
    print(d, e, f)
    print("\n2.")
    print(find_point(a, b, c))
    print(find_point(d, e, f))


if __name__ == "__main__":
    project_2()
