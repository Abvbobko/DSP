import matplotlib.pyplot as plt
from signals import harmonic
import numpy as np


def task2(N, K, phi=0):
    # fig, ax = plt.subplots()
    M = [int(m) for m in np.linspace(K, 2*N, 4*8*2)]  # убрать произведения и вычислять все самому
    if N-1 not in M:
        M.append(N-1)
        M.sort()
    x = []
    for m in M:
        # for n in range(0, m+1):
        n_list = list(range(0, m+1))
        x.append([
            harmonic.harmonic_signal(A=1, f=1, n=n, N=N, phi=phi)
            for n in n_list
        ])
        # ax.plot(n_list, x)
    #plt.show()


if __name__ == '__main__':
    N_test = 64
    K_test = N_test/4
    task2(N=N_test, K=K_test)
