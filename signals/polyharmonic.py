from signals.harmonic import harmonic_signal


def polyharmonic_signal(k, A, f, n, N, phi):
    x = 0
    for j in range(1, k+1):
        x += harmonic_signal(A=A[j], f=f[j], n=n, N=N, phi=phi[j])
    return x
