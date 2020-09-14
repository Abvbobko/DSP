import matplotlib.pyplot as plt
from signals import harmonic


def create_signal(N, A, f, phi, ax, plot_column, out_accuracy=2):
    for i in range(len(A)):
        title = " | ".join([
            f"A: {round(A[i], out_accuracy)}",
            f"f: {round(f[i], out_accuracy)}",
            f"phi: {round(phi[i], out_accuracy)}"
        ])
        ax[i][plot_column].set_title(title)

        n_list = list(range(N))
        x = [
            harmonic.harmonic_signal(A=A[i], f=f[i], n=n, N=N, phi=phi[i])
            for n in n_list
        ]
        ax[i][plot_column].plot(n_list, x)


def series_to_list(num_of_cols, param_name, table):
    return [
        table[f'{param_name}{i}'] for i in range(1, num_of_cols+1)
    ]


def task2(option, storage, N=512):
    SIZE = 5
    fig, ax = plt.subplots(SIZE, 3)

    fig.suptitle('Harmonic signal', fontsize=14, fontweight='bold')
    fig.tight_layout()

    # task 2a
    print("=== task 2.a ===")
    table_a = storage.get_a(option)

    A = table_a.A
    f = table_a.f
    phi = series_to_list(num_of_cols=SIZE, param_name='phi', table=table_a)

    create_signal(N=N, A=[A]*SIZE, f=[f]*SIZE, phi=phi, ax=ax, plot_column=0)

    # task 2b
    print("=== task 2.b ===")
    table_b = storage.get_b(option)

    A = table_b.A
    f = series_to_list(num_of_cols=SIZE, param_name='f', table=table_b)
    phi = table_b.phi

    create_signal(N=N, A=[A]*SIZE, f=f, phi=[phi]*SIZE, ax=ax, plot_column=1)

    # task 2v
    print("=== task 2.c ===")
    table_v = storage.get_v(option)

    A = series_to_list(num_of_cols=SIZE, param_name='A', table=table_v)
    f = table_v.f
    phi = table_v.phi

    create_signal(N=N, A=A, f=[f]*SIZE, phi=[phi]*SIZE, ax=ax, plot_column=2)

    plt.show()
