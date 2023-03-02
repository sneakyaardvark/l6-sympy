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
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - x
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - y

    f1 = sympy.solve(fy, t1)
    f2 = sympy.solve(fy, t2)
    sympy.pprint([f1, f2])


if __name__ == "__main__":
    problem_1b()
