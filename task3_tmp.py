import matplotlib.pyplot as plt
from math import pi
from signals import polyharmonic
import pandas as pd


def task3(storage, option, N):
    table_g = storage.get_g(option)

    # N = 512
    n_list = list(range(N))

    # task 3.1 (просто таблица)
    fig, ax = plt.subplots()
    x = [
        polyharmonic.polyharmonic_signal(k=5, A=table_g.A, N=N, f=table_g.f, n=n, phi=table_g.phi)
        for n in n_list
    ]
    ax.plot(n_list, x)
    plt.show()

    # task 3.2 (изменять phi)
    fig, ax = plt.subplots(5, 2)
    c_offset = pi/4
    d_offset = pd.Series([0, pi/2, pi/3, pi/4, pi], index=[i for i in range(1, 6)])
    phi_const_offset = table_g.phi.copy()
    phi_diff_offset = table_g.phi.copy()
    for i in range(1, 6):
        x1 = [
            polyharmonic.polyharmonic_signal(k=5, A=table_g.A, N=N, f=table_g.f, n=n, phi=phi_const_offset)
            for n in n_list
        ]

        x2 = [
            polyharmonic.polyharmonic_signal(k=5, A=table_g.A, N=N, f=table_g.f, n=n, phi=phi_diff_offset)
            for n in n_list
        ]

        phi_const_offset += c_offset
        phi_diff_offset += d_offset
        ax[i - 1][0].plot(n_list, x1)
        ax[i - 1][1].plot(n_list, x2)
    print(phi_diff_offset)
    plt.show()
