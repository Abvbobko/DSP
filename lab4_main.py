from lab4 import task1, task3
import matplotlib.pyplot as plt
from lab3 import task2 as lab3_task2

if __name__ == "__main__":
    N = 512
    B1 = 100
    B2 = 1
    x = task1.generate_signal(N, B1, B2)
    # task 1
    fig, ax = plt.subplots(3)
    ax[0].plot(list(range(N)), x, label="x")
    _, _, A, phi = lab3_task2.get_spectrum(x, N)

    ax[1].plot(list(range(int(N/2 - 1))), A, label="A")
    ax[2].plot(list(range(int(N / 2 - 1))), phi, label="phi")
    for a in ax:
        a.legend()

    plt.show()

    fig, ax = plt.subplots(3, 3)

    x_avrg = task3.moving_average_with_smoothing_window(x, k=5)
    x_parabola = task3.parabola_of_4_degree(x)
    x_median = task3.median_filtering(x, N, k=55)

    ax[0, 0].plot(list(range(N)), x_avrg, label="avg")

    ax[1, 0].plot(list(range(N)), x_parabola, label="p")

    ax[2, 0].plot(list(range(N)), x_median, label="m")

    _, _, A_avrg, phi_avrg = lab3_task2.get_spectrum(x_avrg, N)
    ax[0, 1].plot(list(range(int(N / 2 - 1))), A_avrg, label="A")
    ax[0, 2].plot(list(range(int(N / 2 - 1))), phi_avrg, label="phi")

    _, _, A_p, phi_p = lab3_task2.get_spectrum(x_parabola, N)
    ax[1, 1].plot(list(range(int(N / 2 - 1))), A_p, label="A")
    ax[1, 2].plot(list(range(int(N / 2 - 1))), phi_p, label="phi")

    _, _, A_m, phi_m = lab3_task2.get_spectrum(x_median, N)
    ax[2, 1].plot(list(range(int(N / 2 - 1))), A_m, label="A")
    ax[2, 2].plot(list(range(int(N / 2 - 1))), phi_m, label="phi")

    for a in ax:
        for a0 in a:
            a0.legend()
    plt.show()
