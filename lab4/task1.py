from math import sin, pi
import random
import matplotlib.pyplot as plt
from lab3 import task2 as lab3_task2
from lab4 import task3


def generate_signal(N, B1, B2):
    if B1 <= B2:
        raise Exception("B1 >> B2 is needed.")
    x = []
    for i in range(N):
        x.append(
            B1*sin(2*pi*i/N) + sum([
                (-1)**random.choice([0, 1])*B2*sin(2*pi*i*j/N) for j in range(50, 71)
            ])
        )
    return x
