import numpy
from math import sin, cos, pi, atan
import matplotlib.pyplot as plt


def tsin(N, A=1):
    return [A*sin(2*pi*I/N) for I in range(N)]


def tcos(N, A=1):
    TSIN = tsin(N, A)
    return [TSIN[(nR + N/4) % N] for nR in range(N)]


def dft(x, N, j):
    A_cj = (2/N)*sum([x[i]*cos(2*pi*j*i/N) for i in range(N)])
    A_sj = (2/N)*sum([x[i]*sin(2*pi*j*i/N) for i in range(N)])
    A_j = (A_cj**2 + A_sj**2)**(1/2)
    phi_j = atan(A_sj/A_cj)
    return A_cj, A_sj, A_j, phi_j


def signal_recovering(N, A, phi):
    y = []
    for i in range(N):
        y.append(sum(
            [A[j]*cos((2*pi*i*j)/N - phi[j]) for j in range(int(N/2 - 1))]
        ))
    return y


def test_signal_generator(N, A=100, f=20, phi=pi/4):
    return [A*cos(2*pi*f*i/N - phi) for i in range(N)]


def task2(x, N):
    A_c, A_s, A, phi = [], [], [], []
    for j in range(int(N / 2 - 1)):
        A_cj, A_sj, A_j, phi_j = dft(x, N, j)

        A_c.append(A_cj)
        A_s.append(A_sj)
        A.append(A_j)
        phi.append(phi_j)

    y = signal_recovering(N, A, phi)

    fig, ax = plt.subplots(3)

    ax[0].set_title('task 1')
    ax[0].plot(list(range(N)), x, c="red", label="x", linewidth=3)
    ax[0].plot(list(range(N)), y, c="green", label="y")

    ax[1].plot(list(range(int(N/2 - 1))), A, label="A")
    ax[2].plot(list(range(int(N / 2 - 1))), phi, label="phi")

    for a in ax:
        a.legend()
    plt.show()
