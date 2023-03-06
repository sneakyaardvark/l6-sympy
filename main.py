import sympy
from math import degrees
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control import control_plots as cplot


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

    # p = sympy.plot(a2[1], show=False)
    # p.show()
    sympy.pprint([a1[0], a2[0]])


def example_2():
    """
    Part II example before problem 2
    """
    s = sympy.symbols("s")
    n = s - 1
    d = s**2 - 3*s + 4
    sys = TransferFunction(n, d, s)
    cplot.bode_plot(sys)


def problem_2b():
    r, s, c, l, w = sympy.symbols("r, s, c, l, w")
    n = r * s * c
    d = (s**2 * l * c + r * c * s + 1)
    h = TransferFunction(n, d, s)
    t = h.num.subs({s: sympy.I * w})  # subs() for TransferFunction doesn't seem to work?


def problem_2c():
    pass


if __name__ == "__main__":
    problem_2b()
