import matplotlib.pyplot as plt
from data import data_storage
from signals import harmonic
from signals import polyharmonic
import task2_tmp
import task3_tmp
import task4_tmp


if __name__ == '__main__':
    option = 1  # int(input())
    storage = data_storage.generate_data()
    # task2_tmp.task2(option=option, storage=storage, N=512)
    # task3_tmp.task3(option=option, storage=storage, N=512)
    task4_tmp.task4(option, storage, N=512, num_of_periods=4)

