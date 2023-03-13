import sympy
from math import degrees

from sympy.physics.control.lti import TransferFunction
from sympy.physics.control import control_plots as cplot
import matplotlib.pyplot as plt


def problem_1a():
    """
    Problem 1 part a
    Prints the two solutions to the terminal
    """
    t1, t2 = sympy.symbols("t1, t2")
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - 2
    # [{t1: ,t2: },{t1: , t2: }]
    answers = sympy.solve([fx, fy], (t1, t2), dict=True)
    print("raw:")
    sympy.pprint(answers)
    print("Degrees:\n(theta1, theta2)")
    # loop through the answers list, convert to degrees, and account for t2 = theta1 + theta2
    for a in answers:
        print(
            (degrees(a[t1].evalf()), degrees(a[t2].evalf()) - degrees(a[t1].evalf()))
        )


def problem_1b():
    """
    Create the plot for Problem 1 part b
    """
    y, t1, t2 = sympy.symbols("y, t1, t2", real=True)
    # given functions
    fx = 4 * sympy.cos(t1) + 3 * sympy.cos(t2) - 6
    fy = 4 * sympy.sin(t1) + 3 * sympy.sin(t2) - y

    # solve function x for t1 and t2
    ft1 = sympy.solve(fx, t1, dict=True)
    ft2 = sympy.solve(fx, t2, dict=True)

    # substitute functions for t1 and t2 into function y
    # so we can have t1 and t2 purely in terms of y
    f1 = fy.subs(ft1[0])
    a1 = sympy.solve(f1, t2)
    f2 = fy.subs(ft2[0])
    a2 = sympy.solve(f2, t1)

    # account for t2 = theta1 + theta2
    a2 = a2[0] - a1[0]

    # rad -> deg
    a1 = (a1[0] * 180) / sympy.pi
    a2 = (a2 * 180) / sympy.pi

    # plot
    plt_theta1 = sympy.plot(a1, (y, 0.1, 3.6), show=False)
    plt_theta1.ylabel = r"$\theta_1$ (degrees)"
    plt_theta1.xlabel = r"$\it{y}$ (feet)"
    plt_theta2 = sympy.plot(a2, (y, 0.1, 3.6), show=False)
    plt_theta2.ylabel = r"$\theta_2$ (degrees)"
    plt_theta2.xlabel = r"$\it{y}$ (feet)"
    sympy.plotting.PlotGrid(2, 1, plt_theta1, plt_theta2)


def problem_2b():
    """
    Create the plot for Problem 2 part b
    """
    r, s, c, l, w = sympy.symbols("r, s, c, l, w", real=True)
    numer = (r * w) / l
    denom = sympy.sqrt((1 / (l * c) - w ** 2) ** 2 + (r * w / l) ** 2)
    h = numer / denom
    values = {
        c: 10e-6,
        l: 5e-3,
    }
    w_range = (w, 100, 100000)  # 100 to 100k rad/s
    h = h.subs(values)  # sub given C and L
    h_r10 = h.subs({r: 10})
    h_r100 = h.subs({r: 100})
    h_r1k = h.subs({r: 1000})

    # plot
    plt_r = sympy.plot(h_r10, w_range, show=False, legend=True, label="R=10")
    plt_r100 = sympy.plot(h_r100, w_range, show=False, label="R=100")
    plt_r1k = sympy.plot(h_r1k, w_range, show=False, label="R=1k")
    plt_r.extend(plt_r100)
    plt_r.extend(plt_r1k)
    plt_r.title = r"Transfer Function $\it{H}$"
    plt_r.xlabel = r"$\it{\omega}$ (rad/s)"
    plt_r.ylabel = r"$\it{H}(\omega)$"
    plt_r.show()


def problem_2cd():
    """
    Create plots for Problem 2 parts c and d
    """
    s = sympy.symbols("s")
    r, c, l = sympy.symbols("r, c, l", real=True)
    numer = r
    denom = r + (s * l) + (1 / (s * c))
    h = TransferFunction(numer, denom, s)
    values = {
        c: 10e-6,
        l: 5e-3,
    }
    h = h.subs(values)
    r_values = [10, 100, 1000]

    impulse_data = {}
    step_data = {}
    for i in r_values:
        f = h.subs({r: i})
        # part c
        cplot.bode_magnitude_plot(f, freq_unit="rad/sec")

        # part d
        # use numerical_data functions to make plotting them together easier
        impulse_data[i] = cplot.impulse_response_numerical_data(f, upper_limit=0.005)
        step_data[i] = cplot.step_response_numerical_data(f, upper_limit=0.05)

    def plot_from_data(data: dict, plot_title: str):
        """
        Plot data from dict of numerical_data (x, y) tuples
        :param data: dict of (x, y) tuples
        :param plot_title: title for the plot
        """
        colors = {
            10: 'b',
            100: 'g',
            1000: 'r'
        }
        for k, v in data.items():
            x, y = v
            plt.plot(x, y, color=colors[k], label=f"R={k}")
        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(plot_title)
        plt.show()

    plot_from_data(impulse_data, "Impulse Response")
    plot_from_data(step_data, "Step Response")


def problem_2e():
    """
    Print the natural response function for v_r
    """
    t, r, l, c = sympy.symbols("t, r, l, c", real=True)
    v_r, v_i = sympy.symbols("v_r, v_i", cls=sympy.Function)
    deriv2_v_r = sympy.Derivative(v_r(t), t, 2)
    deriv_v_r = sympy.Derivative(v_r(t), t)
    f = deriv2_v_r + (r / l) * deriv_v_r + (v_r(t) / (l * c))
    ans = sympy.dsolve(f)
    sympy.pprint(ans)


if __name__ == "__main__":
    sympy.init_printing(use_unicode=True)
    # change this function call to run a specific problem. We're not fancy here today.
    problem_2e()
