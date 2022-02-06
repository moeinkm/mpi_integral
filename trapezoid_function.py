import math
from datetime import datetime


def f(x):
    """
    the function we want to calculate its integral
    :param x: x
    :return: f(x) which here is cos(x)
    """
    return math.cos(x)


def trapezoid(a, b, n, h):
    """
    trapezoid method calculates integral of f(x) approximately between a and b
    by increasing n it get more and more accurate
    :param a: starting intersection node
    :param b: ending intersection node
    :param n: number of nodes
    :param h: length of each section
    :return: integral of f(x)
    """

    integral = (f(a) + f(b)) / 2

    x = a
    for i in range(1, int(n)):
        x = x + h
        integral = integral + f(x)

    return integral * h


if __name__ == '__main__':
    # to compare run time with and without mpi
    start = datetime.now()
    trapezoid(0, 10, 1024, 1/1024)
    end = datetime.now()
    print(f'elapsed time: {end - start}')