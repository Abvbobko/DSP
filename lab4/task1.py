from math import sin, pi
import random
import matplotlib.pyplot as plt
from lab3 import task2 as lab3_task2
from lab4 import task3


def generate_signal(N, B1, B2):
    if B1 <= B2:
        raise Exception("B1 >> B2 is needed.")
    x = []
    for i in range(N):
        x.append(
            B1*sin(2*pi*i/N) + sum([
                (-1)**random.choice([0, 1])*B2*sin(2*pi*i*j/N) for j in range(50, 71)
            ])
        )
    return x


if __name__ == "__main__":
    N = 512
    B1 = 100
    B2 = 1
    x = generate_signal(N, B1, B2)

    fig, ax = plt.subplots(4)
    ax[0].set_title('task 1')
    ax[0].plot(list(range(N)), x, label="x")

    _, _, A, phi = lab3_task2.get_spectrum(x, N)

    # ax[1].plot(list(range(int(N/2 - 1))), A, label="A")
    # ax[2].plot(list(range(int(N / 2 - 1))), phi, label="phi")
    x_avrg = task3.moving_average_with_smoothing_window(x, k=5)
    x_parabola = task3.parabola_of_4_degree(x)
    x_median = task3.median_filtering(x, N, k=55)

    ax[1].plot(list(range(N)), x_avrg, label="avg")
    ax[2].plot(list(range(N)), x_parabola, label="p")
    ax[3].plot(list(range(N)), x_median, label="m")

    for a in ax:
        a.legend()
    plt.show()
