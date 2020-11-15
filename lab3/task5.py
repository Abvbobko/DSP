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


def task5(x):
    fig, ax = plt.subplots(4)
    ax[0].set_title("task 3-4")
    ax[0].plot(list(range(len(x))), x, c="black", linewidth=3, label="x")
    ax[1].plot(list(range(len(x))), low_pass_filter(x), c="red", linewidth=1, label="hx")
    ax[2].plot(list(range(len(x))), high_pass_filter(x), c="orange", linewidth=1, label="lx")
    ax[3].plot(list(range(len(x))), band_pass_filter(x), c="green", linewidth=1, label="bx")

    for a in ax:
        a.legend()
    plt.show()

