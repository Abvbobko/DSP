import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fft import fft, ifft

N = 64
K = 64
M = 64
fi = 0

X = []
Y = []


def Xn(n):
    return math.sin((2 * math.pi * n) / N + fi)


def amplitude_by_fourier(values):
    values = list(values)
    N = len(values)
    sin_sum, cos_sum = 0, 0
    for i, y in enumerate(values):
        angle = 2 * math.pi * i / N
        sin_sum += y * math.sin(angle)
        cos_sum += y * math.cos(angle)
    sin_sum *= 2 / N
    cos_sum *= 2 / N
    return math.sqrt(sin_sum ** 2 + cos_sum ** 2)


def sum_of_Xn(power):
    ans = 0
    global Y
    for i in Y:
        ans += i ** power
    return ans


def getD_a():
    return math.sqrt(1 / (M + 1) * sum_of_Xn(2))


def getD_b():
    return math.sqrt(abs(
        ((1 / (M + 1)) * sum_of_Xn(2))
        -
        ((1 / (M + 1)) * (sum_of_Xn(1) ** 2))
    ))


def main_t(Da, Db, Dc, m):
    X.clear()
    Y.clear()
    global M
    M = m
    for i in range(0, m, 1):
        X.append(i)
        Y.append(Xn(i))
    Da.append(abs(1 - amplitude_by_fourier(Y)))
    Db.append(abs(0.707 - getD_a()))
    Dc.append(abs(0.707 - getD_b()))
    # print("Math exp1: ", getD_a())
    # print("Math exp2: ", getD_b())
    # print("delta math error1: ", 0.707 - getD_a())
    # print("delta math error2: ", 0.707 - getD_b())
    # print("delta amp error: ", abs(1 - amplitude_by_fourier(Y)))


def main(args):
    global N, K, M, fi
    N = 256
    K = N / 4
    M = N - 1
    # if '-fi' in args:
    # fi = 3*math.pi / 4

    D_A_x = []
    D_A_y_a = []
    D_A_y_b = []
    D_A_y_c = []
    for i in range(int(K), 2 * N, 1):
        main_t(D_A_y_a, D_A_y_b, D_A_y_c, i)
        D_A_x.append(i)

    plt.plot(D_A_x, D_A_y_a, label='f={}'.format(str('Hello')))
    plt.plot(D_A_x, D_A_y_b, label='f={}'.format(str('Hello')), c="green")
    # plt.plot(D_A_x, D_A_y_c, label='f={}'.format(str('Hello')))
    plt.show()


if __name__ == "__main__":
    args = sys.argv
    args = []
    main(args)