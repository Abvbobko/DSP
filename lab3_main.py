from lab3 import task2, task3, task5
from math import pi


if __name__ == '__main__':
    N = 128  # int(input())

    # task 2
    x = task2.test_signal_generator(N)
    task2.task2(x, N)

    # task 3
    B = [2, 3, 5, 9, 10, 12, 15]
    phi = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]
    x = task3.generate_polyharmonic_test_signal(N, B, phi)
    task3.task3(x, N)

    # task 4, 5
    task5.task5(x)
