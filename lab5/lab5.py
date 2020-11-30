import matplotlib.pyplot as plt
from lab3 import task2, task3
from math import pi, sin, cos
from scipy import signal
import numpy as np


def corr(f, g, N):
    r = []
    for n in range(N):
        r.append(-sum([
            f(n+k, N)*g(k, N) for k in range(n)
        ]))
    return r


def signal_generator(k, N, A=100, f=8, phi=pi/4):
    return A*cos(2*pi*f*k/N - phi)


def get_correlation(sig1, sig2):
    n1 = len(sig1)
    n2 = len(sig2)

    correlation = []
    maxSum = 0
    for i in range(0, n1 + n2 - 1):
        subsig1 = sig1[0 if (i - n2 + 1) < 0 else i - n2 + 1:  i + 1 if i < n1 else n1]
        subsig2 = sig2[0 if (n2 - i - 1) < 0 else n2 - i - 1:  n2 if i < n1 else n1 - i + n2 - 1]
        item_sum = np.sum(np.multiply(subsig1, subsig2))
        maxSum = max(item_sum, maxSum)
        correlation.append(item_sum)
    return list(range(-n2 + 1, n1)), np.array(correlation) / maxSum


if __name__ == '__main__':
    N = 128  # int(input())
    fig, ax = plt.subplots(2, 2)
    x = [signal_generator(k, N, A=100, f=8) for k in range(N)]
    y = [signal_generator(k, N, A=150, f=5) for k in range(N)]

    corr1 = signal.correlate(x, x, mode='full')

    auto = get_correlation(x, x)
    cross = get_correlation(x, y)

    ax[0, 0].plot(list(range(N)), x, label="x")
    ax[0, 1].plot(list(range(N)), y, label="y", c="orange")
    ax[1, 0].plot(auto[0], auto[1], label="auto")
    ax[1, 1].plot(cross[0], cross[1], label="cross")
    for a in ax:
        for a_item in a:
            a_item.legend()
    plt.show()
