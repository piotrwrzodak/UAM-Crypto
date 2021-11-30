from project_2.piotr_wrzodak_16_2_1 import generate_elliptic_curve
from project_2.piotr_wrzodak_16_2_2 import find_point
from project_2.piotr_wrzodak_16_2_3 import opposite_point
from project_2.piotr_wrzodak_16_2_4 import addPoints
from project_2.piotr_wrzodak_16_2_5 import multiplePoint


def project_2():
    print("1.")
    a, b, c = generate_elliptic_curve()
    print(a, b, c)
    d, e, f = generate_elliptic_curve()
    print(d, e, f)
    print("\n2.")
    print(find_point(a, b, c))
    print(find_point(d, e, f))
    print("\n3.")
    print(opposite_point(3, 2, 7))
    print(opposite_point(1, 4, 5))
    print("\n4.")
    print(addPoints(68719476731, 2645887931, 63508942644, "infty", "infty", 15593395299, 42666859491))
    print(addPoints(68719476731, 2645887931, 63508942644, 56174319723, 50334202836, 15593395299, 42666859491))
    print(addPoints(68719476731, 20850939805, 59338401596, 3789244612, 16129056986, 3789244612, 52590419745))
    print(addPoints(68719476731, 49710749469, 5286130045, 24069898531, 10203122697, 24069898531, 10203122697))
    print("\n5.")
    print(multiplePoint(11, 3, 5, 0, 4, 4))


if __name__ == "__main__":
    project_2()
