from project_1.piotr_wrzodak_16_1_1 import euclidean_algorithm


def addPoints(p, a, b, x1, y1, x2, y2):
    if x1 and y1 == "infty":
        return [x2, y2]
    if x2 == "infty" and y2 == "infty":
        return [x1, y1]
    if x1 % p == x2 % p and y1 % p == -y2 % p:
        return ["infty", "infty"]

    else:
        if x1 % p != x2 % p:
            s = ((y1 - y2) * euclidean_algorithm(x1 - x2, p)) % p
        elif x1 % p == x2 % p and y1 % p == y2 % p:
            s = (((3 * pow(x1, 2, p) % p) + a) * euclidean_algorithm(2 * y1, p)) % p
        else:
            return
        x3 = (pow(s, 2, p) - x1 - x2) % p
        y3 = ((s * (x1 - x3) % p) - y1) % p
        return [x3, y3]


if __name__ == "__main__":
    print(addPoints(68719476731, 2645887931, 63508942644, "infty", "infty", 15593395299, 42666859491))
    print(addPoints(68719476731, 2645887931, 63508942644, 56174319723, 50334202836, 15593395299, 42666859491))
    print(addPoints(68719476731, 20850939805, 59338401596, 3789244612, 16129056986, 3789244612, 52590419745))
    print(addPoints(68719476731, 49710749469, 5286130045, 24069898531, 10203122697, 24069898531, 10203122697))
