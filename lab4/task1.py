from math import sin, pi
import random
import matplotlib.pyplot as plt
from lab3 import task2 as lab3_task2


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
    B2 = 5
    x = generate_signal(N, B1, B2)

    fig, ax = plt.subplots(3)
    ax[0].set_title('task 1')
    ax[0].plot(list(range(N)), x, label="x")

    _, _, A, phi = lab3_task2.get_spectrum(x, N)

    ax[1].plot(list(range(int(N/2 - 1))), A, label="A")
    ax[2].plot(list(range(int(N / 2 - 1))), phi, label="phi")

    for a in ax:
        a.legend()
    plt.show()
