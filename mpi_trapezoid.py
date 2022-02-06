from mpi4py import MPI
from trapezoid_function import trapezoid
from datetime import datetime


comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()
start = datetime.now()

a = 0.0  # starting point
b = 10.0  # end point
n = 1024  # number of points
dest = 0  # destination process which will be adding up everything
total = -1.0  # result (-1.0 is initial invalid value)

h = (b - a) / n  # length of each section which is same for all processes
local_n = n / p  # number of trapezoids

local_a = a + my_rank * local_n * h  # a point for each process
local_b = local_a + local_n * h  # b point for each process
integral = trapezoid(local_a, local_b, local_n, h)  # each process will calculate its integral

# do the add up in process 0
if my_rank == 0:
    total = integral
    for source in range(1, p):
        integral = comm.recv(source=source)  # process 0 receives integral from another sources to do the add up
        print(f'rank: {my_rank}, <- {source}, integral: {integral}')
        total = total + integral
else:
    print(f'{my_rank} -> {dest}, integral: {integral}')
    comm.send(integral, dest=0)  # send integral to process 0 to do the add up

if my_rank == 0:
    end = datetime.now()
    print(f'with n={n} trapezoids integral from {a} to {b} = {total} with elapsed time: {end - start}')

MPI.Finalize()
