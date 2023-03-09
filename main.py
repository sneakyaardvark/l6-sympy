import sympy
from math import degrees

from sympy.physics.control.lti import TransferFunction
from sympy.physics.control import control_plots as cplot
from numpy import linspace

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


def problem_1b2():
    x, y, t1, t2 = sympy.symbols("x, y, t1, t2")
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - y
    # ans = [sympy.solve([fx, fy.subs({y: i})], (t1, t2)) for i in linspace(0.1, 3.6)]
    sympy.pprint(sympy.solve([fx, fy.subs({y: 2})], (t1, t2)))


def problem_1b():
    x, y, t1, t2 = sympy.symbols("x, y, t1, t2")
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - y

    ft1 = sympy.solve(fx, t1, dict=True)
    ft2 = sympy.solve(fx, t2, dict=True)

    sympy.pprint(ft1)
    sympy.pprint(ft2)

    # f1 = sympy.solve([ft, fy], t2)
    f1 = fy.subs(ft1[1])
    a1 = sympy.solve(f1, t2)
    f2 = fy.subs(ft2[1])
    a2 = sympy.solve(f2, t1)

    # sympy.pprint([a1, a2])

    plt_theta1 = sympy.plot(a1[0], (y, 0.1, 3.6), show=False)
    plt_theta2 = sympy.plot(a2[0], (y, 0.1, 3.6), show=False)
    sympy.plotting.PlotGrid(2, 1, plt_theta1, plt_theta2)
    # sympy.pprint([a1[0], a2[0]])


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
    r, s, c, l, w = sympy.symbols("r, s, c, l, w", real=True)
    n = (r*w)/l
    d = sympy.sqrt((1 / (l * c) - w**2)**2 + (r*w/l)**2)
    h = n / d
    values = {
        c: 10e-6,
        l: 5e-3,
    }
    w_range = (w, 100, 100000)
    h = h.subs(values)
    h_r10 = h.subs({r: 10})
    h_r100 = h.subs({r: 100})
    h_r1k = h.subs({r: 1000})
    plt = sympy.plot(h_r10, w_range, show=False, legend=True, label="R=10")
    plt_r100 = sympy.plot(h_r100, w_range, show=False, label="R=100")
    plt_r1k = sympy.plot(h_r1k, w_range, show=False, label="R=1k")
    plt.extend(plt_r100)
    plt.extend(plt_r1k)
    plt.title = r"Transfer Function $\it{H}$"
    plt.xlabel = r"$\it{\omega}$ (rad/s)"
    plt.ylabel = r"$\it{H}(\omega)$"
    plt.show()


def problem_2c():
    r, s, c, l, w = sympy.symbols("r, s, c, l, w", real=True)
    n = (r * w) / l
    d = sympy.sqrt((1 / (l * c) - w ** 2) ** 2 + (r * w / l) ** 2)
    h = TransferFunction(n, d, w)
    values = {
        c: 10e-6,
        l: 5e-3,
    }
    h = h.subs(values)
    r_values = [10, 100, 1000]
    for i in r_values:
        f = h.subs({r: i})
        cplot.bode_magnitude_plot(f)
        # bp = cplot.impulse_response_plot(f, show=False)
        # bp.show()

        # part d
        # cplot.impulse_response_plot(f)


def problem_2e():
    v_r, t, r, l, c, v_i = sympy.symbols("v_r, t, r, l, c, v_i")
    diff = sympy.Derivative()


if __name__ == "__main__":
    problem_1b2()
