from data import data_storage
import task2_tmp
import task3_tmp
import task4_tmp


if __name__ == '__main__':
    option = int(input("Enter an option: "))
    N = 512  # int(input())
    storage = data_storage.generate_data()
    task2_tmp.task2(option=option, storage=storage, N=N)
    task3_tmp.task3(option=option, storage=storage, N=N)
    task4_tmp.task4(option, storage, N=N, num_of_periods=4)

