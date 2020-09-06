import math


def harmonic_signal(A, f, n, N, phi):
    """
    Функция возвращает гармонический сигнал

    :param A: амплитуда
    :param f: частота
    :param n: 0..N-1
    :param N: 512, 1024, 2048, ...
    :param phi: начальная фаза в радианах
    :return:
    """
    return A * math.sin(2*math.pi*f*n / N + phi)
