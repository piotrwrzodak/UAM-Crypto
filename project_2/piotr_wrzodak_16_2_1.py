import random


def calc_discriminant(a, b):
    # d = -16 * (4 * pow(a, 3) + 27 * pow(b, 2))
    d = 4 * pow(a, 3) + 27 * pow(b, 2)
    return d


def generate_variables(p):
    a = random.randrange(p - 1)
    b = random.randrange(p - 1)
    return [a, b]


def generate_elliptic_curve():
    p = pow(2, 315) - 465
    mod_prime = p % 4
    print("\nprime:", p, "mod_prime:", mod_prime)

    a, b = generate_variables(p)
    d = calc_discriminant(a, b)

    while d % p == 0:
        a, b = generate_variables(p)
        d = calc_discriminant(a, b)
    print("d:", d)
    print("modulo:", d % p)

    print(f'y^2 = x^3 + {a}x + {b} (mod {p})')

    return [a, b, p]


if __name__ == "__main__":
    print(generate_elliptic_curve())
    print(generate_elliptic_curve())
