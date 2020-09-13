import matplotlib.pyplot as plt
from math import pi
from signals import polyharmonic
import pandas as pd


def create_signal(k, N, A, f, phi, ax, plot_column):
    n_list = list(range(N))
    # for i in range(len(A)):
    x = [
        polyharmonic.polyharmonic_signal(k=k, A=A, N=N, f=f, n=n, phi=phi)
        for n in n_list
    ]
    ax[plot_column].plot(n_list, x)


def task3(storage, option, N):
    SIZE = 5
    table_g = storage.get_g(option)

    # task 3.1 (просто таблица)
    fig, ax = plt.subplots()
    create_signal(k=5, A=table_g.A, N=N, f=table_g.f, phi=table_g.phi, ax=[ax], plot_column=0)

    plt.show()

    # task 3.2 (изменять phi)
    fig, ax = plt.subplots(SIZE, 2)

    c_offset = pi/4
    d_offset = pd.Series([0, pi/2, pi/3, pi/4, pi], index=[i for i in range(1, SIZE+1)])
    phi_const_offset = table_g.phi.copy()
    phi_diff_offset = table_g.phi.copy()

    for i in range(1, SIZE+1):
        create_signal(
            k=5, N=N, ax=ax[i-1],
            A=table_g.A,
            f=table_g.f,
            phi=phi_const_offset,
            plot_column=0
        )
        create_signal(
            k=5, N=N, ax=ax[i-1],
            A=table_g.A,
            f=table_g.f,
            phi=phi_diff_offset,
            plot_column=1
        )
        phi_const_offset += c_offset
        phi_diff_offset += d_offset

    plt.show()
