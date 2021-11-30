from project_2.piotr_wrzodak_16_2_1 import generate_elliptic_curve
from project_2.piotr_wrzodak_16_2_2 import find_point
from project_2.piotr_wrzodak_16_2_4 import addPoints


def multiplePoint(p, a, b, x, y, n):
    q = [x, y]
    r = ["infty", "infty"]
    while n > 0:
        if n % 2 == 1:
            r = addPoints(p, a, b, r[0], r[1], q[0], q[1])
            n = n - 1
        q = addPoints(p, a, b, q[0], q[1], q[0], q[1])
        n = n // 2
    return r


if __name__ == "__main__":
    print(multiplePoint(11, 3, 5, 0, 4, 4))
    print(multiplePoint(1298074214633706907132624082305003, 228534005990621198360294597781867, 569902189632523536847978118572132, 149381772199891494705202718572565, 409260229456564272828054179242535, 1298074214633706907132624082305000))
