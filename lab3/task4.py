import numpy as np
import lab3.task2 as task2
import lab3.task3 as task3
from math import pi


def dft_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def fft(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return dft_slow(x)
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,
                               X_even + factor[int(N / 2):] * X_odd])


if __name__ == '__main__':
    N = 128
    B = [2, 3, 5, 9, 10, 12, 15]
    phi = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]
    x = task3.generate_polyharmonic_test_signal(N, B, phi)
    print(fft(x))
