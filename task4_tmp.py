import matplotlib.pyplot as plt
from signals import polyharmonic
import numpy as np
import pandas as pd


def generate_parameter(start_values, n, proportion=1.2, num_of_periods=1):
    lin_func_param = [np.linspace(v, proportion**num_of_periods * v, n) for v in start_values]
    result = []
    for i in range(len(lin_func_param[0])):
        one_step_values = []
        for j in range(len(lin_func_param)):
            one_step_values.append(lin_func_param[j][i])
        result.append(
            pd.Series(
                one_step_values,
                index=[index for index in range(1, len(start_values) + 1)]
            )
        )
    return result


def task4(option, storage, N=512, num_of_periods=1):
    table_g = storage.get_g(option)

    n_list = list(range(num_of_periods * N))
    x = []

    A = generate_parameter(table_g.A, len(n_list), proportion=1.2, num_of_periods=num_of_periods)
    f = generate_parameter(table_g.f, len(n_list), proportion=1.2, num_of_periods=num_of_periods)
    phi = generate_parameter(table_g.phi, len(n_list), proportion=1.2, num_of_periods=num_of_periods)

    period = [[], []]
    fig, ax = plt.subplots()
    for i in range(len(n_list)):
        signal_value = polyharmonic.polyharmonic_signal(
            k=5,
            A=A[i],
            N=N,
            f=f[i],
            n=n_list[i],
            phi=phi[i])
        if (i % N == 0) and (i != 0):
            period[0].append(i)
            period[1].append(signal_value)
        x.append(signal_value)

    ax.plot(n_list, x)
    ax.scatter(period[0], period[1], color='r')
    plt.show()
