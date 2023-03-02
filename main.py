import sympy
from math import degrees


def problem_1a():
    x, y, t1, t2 = sympy.symbols("x, y, t1, t2")
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - 2

    # [(t1, t2),(t1, t2)]
    answers = sympy.solve([fx, fy], (t1, t2))
    print("(theta1, theta2)")
    for a in answers:
        print(
            (degrees(a[0].evalf()), degrees(a[1].evalf()) - degrees(a[0].evalf()))
        )


def problem_1b():
    x, y, t1, t2 = sympy.symbols("x, y, t1, t2")
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - y

    ft1 = sympy.solve(fx, t1, dict=True)
    ft2 = sympy.solve(fx, t2, dict=True)

    # f1 = sympy.solve([ft, fy], t2)
    f1 = fy.subs(ft1[1])
    a1 = sympy.solve(f1, t2)
    f2 = fy.subs(ft2[1])
    a2 = sympy.solve(f2, t1)
    sympy.pprint([a1[0], a2[0]])


if __name__ == "__main__":
    problem_1b()
