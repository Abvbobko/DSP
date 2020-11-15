

def average_square_value_a(x, M):
    return (sum([x_item*x_item for x_item in x])/(M+1))**(1/2)


def average_square_value_b(x, M):
    return (average_square_value_b(x, M)**2 - (sum(x)/(M+1)))**(1/2)

