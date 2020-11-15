from lab3.task4 import fft
from scipy.fft import ifft
from math import pi
from lab3 import task3
import matplotlib.pyplot as plt

LOW_BORDER = 5
HIGH_BORDER = 20


def pass_filter(x, filter_func):
    fx = fft(x)
    for i in range(len(x)):
        if filter_func(x[i]):
            fx[i] = 0
    return ifft(fx)


def low_pass_filter(x):
    return pass_filter(x, lambda t: t > LOW_BORDER)


def high_pass_filter(x):
    return pass_filter(x, lambda t: t < HIGH_BORDER)


def band_pass_filter(x):
    return pass_filter(x, lambda t: not (LOW_BORDER < t < HIGH_BORDER))


if __name__ == '__main__':
    N = 128
    B = [2, 3, 5, 9, 10, 12, 15]
    phi = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]
    x = task3.generate_polyharmonic_test_signal(N, B, phi)
    plt.plot(list(range(len(x))), x, c="black", linewidth=3, label="x")
    plt.plot(list(range(len(x))), low_pass_filter(x), c="red", linewidth=1, label="hx")
    plt.plot(list(range(len(x))), high_pass_filter(x), c="orange", linewidth=1, label="lx")
    plt.plot(list(range(len(x))), band_pass_filter(x), c="green", linewidth=1, label="bx")
    plt.legend()
    plt.show()
