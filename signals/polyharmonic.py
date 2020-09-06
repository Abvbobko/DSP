from signals.harmonic import harmonic_signal


def polyharmonic_signal(k, A, f, n, N, phi):
    x = 0
    for i in range(k):
        x += harmonic_signal(A=A[i], f=f[i], n=n, N=N, phi=phi[i])
    return x
