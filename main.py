import matplotlib.pyplot as plt
from data import data_storage
from signals import harmonic


if __name__ == '__main__':
    option = 1  # int(input())
    storage = data_storage.generate_data()

    # task 2a
    table_a = storage.get_a(option)

    fig, ax = plt.subplots(5, 3)
    A = table_a.A
    f = table_a.f
    N = 512
    for i in range(1, 6):
        n_list = list(range(N))

        x = [
            harmonic.harmonic_signal(A=A, f=f, n=n, N=N, phi=table_a[f'phi{i}'])
            for n in n_list
        ]

        ax[i - 1][0].plot(n_list, x)

    # task 2b
    table_b = storage.get_b(option)
    A = table_b.A
    phi = table_b.phi
    for i in range(1, 6):
        n_list = list(range(N))

        x = [
            harmonic.harmonic_signal(A=A, f=table_b[f'f{i}'], n=n, N=N, phi=phi)
            for n in n_list
        ]

        ax[i - 1][1].plot(n_list, x)

    # task 2v
    table_v = storage.get_v(option)
    f = table_v.f
    phi = table_v.phi
    for i in range(1, 6):
        n_list = list(range(N))

        x = [
            harmonic.harmonic_signal(A=table_v[f'A{i}'], f=f, n=n, N=N, phi=phi)
            for n in n_list
        ]

        ax[i - 1][2].plot(n_list, x)

    plt.show()
