

def moving_average_with_smoothing_window(x, k, win_size=9):
    # if k % 2 != 1:
    #     raise Exception("K must be odd.")
    m = int((k-1)/2)
    new_x = []
    for i in range(len(x)):
        iter_k = k
        left_bound = i - m
        right_bound = i + m
        if (left_bound < 0) or (right_bound > len(x) - 1):
            left_bound = i - (min(i-1, len(x)-i))
            right_bound = i + (min(i - 1, len(x) - i))
            iter_k = 2*(min(i-1, len(x)-i)) - 1
        new_x.append(
            sum([
                x[j] for j in range(left_bound, right_bound)
            ])/iter_k
        )
    return new_x


def parabola_of_4_degree(x):
    new_x = []
    for i in range(len(x)):
        if (i == 0) or (i == len(x) - 1):
            new_x.append(131 * x[i]/231)
        elif (i == 1) or (i == len(x) - 2):
            new_x.append(
                (75 * x[i - 1] + 131 * x[i] + 75 * x[i + 1]) / 231
            )
        elif (i == 2) or (i == len(x) - 3):
            new_x.append(
                (30 * x[i - 2] + 75 * x[i - 1] + 131 * x[i] + 75 * x[i + 1] - 30 * x[i + 2]) / 231
            )
        else:
            new_x.append(
                (5*x[i-3] - 30*x[i-2] + 75*x[i-1] + 131*x[i] + 75*x[i+1] - 30*x[i+1] + 5*x[i+3])/231
            )

    return new_x


def median_filtering(x, N, k, win_size=5):

    return moving_average_with_smoothing_window(x, k=(N-2*k), win_size=win_size)

