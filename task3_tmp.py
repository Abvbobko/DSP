import matplotlib.pyplot as plt
from math import pi
from signals import polyharmonic
import pandas as pd


def create_signal(k, N, A, f, phi, ax):
    n_list = list(range(N))
    x = [
        polyharmonic.polyharmonic_signal(k=k, A=A, N=N, f=f, n=n, phi=phi)
        for n in n_list
    ]
    ax.plot(n_list, x)


def task3(storage, option, N):
    SIZE = 5
    table_g = storage.get_g(option)

    # task 3.1 (просто таблица)
    fig = plt.figure()
    fig.suptitle('Polyharmonic signal (table / phi const change / phi diff change)', fontsize=14, fontweight='bold')

    fig_size = (5, 7)
    ax1 = plt.subplot2grid(fig_size, (0, 0), rowspan=3, colspan=3)
    print("=== task 3.1 ===")
    print('A:\n', table_g.A)
    print('f:\n', table_g.f)
    print('phi:\n', table_g.phi)
    create_signal(k=5, A=table_g.A, N=N, f=table_g.f, phi=table_g.phi, ax=ax1)

    # task 3.2 (изменять phi)
    print("=== task 3.2 ===")

    c_offset = pi/4
    d_offset = pd.Series([0, pi/2, pi/3, pi/4, pi], index=[i for i in range(1, SIZE+1)])
    phi_const_offset = table_g.phi.copy()
    phi_diff_offset = table_g.phi.copy()
    print("A:\n", table_g.A)
    print("f:\n", table_g.f)
    for i in range(1, SIZE+1):
        print(f"phi_const_{i}:\n", phi_const_offset)
        print(f"phi_diff_{i}:\n", phi_diff_offset)
        create_signal(
            k=5, N=N, ax=plt.subplot2grid(fig_size, (i-1, 3), colspan=2),
            A=table_g.A,
            f=table_g.f,
            phi=phi_const_offset
        )
        create_signal(
            k=5, N=N, ax=plt.subplot2grid(fig_size, (i-1, 5), colspan=2),
            A=table_g.A,
            f=table_g.f,
            phi=phi_diff_offset
        )
        phi_const_offset += c_offset
        phi_diff_offset += d_offset

    fig.tight_layout()
    plt.show()
