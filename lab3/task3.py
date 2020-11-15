import lab3.task2 as task2
from math import cos, pi
import random
import matplotlib.pyplot as plt


def generate_polyharmonic_test_signal(N, B, phi,  num_of_harmonics=30):
    x = []
    for i in range(N):
        B_j = random.choice(B)
        phi_j = random.choice(phi)
        x.append(sum(
            [B_j*cos(2*pi*j*i/N - phi_j) for j in range(1, num_of_harmonics)]
        ))
    return x


def signal_recovering(N, A, phi):
    y = []
    for i in range(N):
        y.append(A[0]/2 + sum(
            [A[j]*cos((2*pi*i*j)/N - phi[j]) for j in range(1, int(N/2 - 1))]
        ))
    return y


def task3(x, N):
    A_c, A_s, A, phi = [], [], [], []
    for j in range(int(N / 2 - 1)):
        A_cj, A_sj, A_j, phi_j = task2.dft(x, N, j)

        A_c.append(A_cj)
        A_s.append(A_sj)
        A.append(A_j)
        phi.append(phi_j)

    y1 = signal_recovering(N, A, phi)
    y2 = signal_recovering(N, A, len(phi) * [0])
    # plt.plot(list(range(int(N/2 - 1))), A)
    # plt.plot(list(range(int(N / 2 - 1))), phi)
    fig, ax = plt.subplots(3)

    ax[0].set_title('task 2')
    ax[0].plot(list(range(N)), x, c="red", label="x", linewidth=3)
    ax[0].plot(list(range(N)), y1, c="green", label="y1", linewidth=2)
    ax[0].plot(list(range(N)), y2, c="black", label="y2", linewidth=1)

    ax[1].plot(list(range(int(N/2 - 1))), A, label="A")
    ax[2].plot(list(range(int(N/2 - 1))), phi, label="зрш")

    for a in ax:
        a.legend()

    plt.show()
