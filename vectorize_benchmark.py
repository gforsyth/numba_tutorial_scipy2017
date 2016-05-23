from numba import vectorize, float64
import numpy
import timeit

@vectorize
def u_serial(uplus, uminus, dx):
    return (uplus - uminus)/(2*dx)

@vectorize([float64(float64, float64, float64)], target='parallel')
def u_parallel(uplus, uminus, dx):
    return (uplus - uminus)/(2*dx)

array_size = [100, 1000, 5000, 10000]
#array_size = [5, 10, 15, 20]

def serial_time(n):
    a = numpy.ones((n,n), dtype=numpy.float64)
    u_serial(a, a, .5)

def parallel(n):
    a = numpy.ones((n,n), dtype=numpy.float64)
    u_parallel(a, a, .5)

print('{:-^60}'.format('Serial runs'))
for n in array_size:
    print('{:-^60}'.format('Serial run with n={}'.format(n)))
    t = timeit.Timer('serial_time(n)', globals=globals())
    reps = 10
    print([i/reps for i in t.repeat(number=reps)])

    print('{:-^60}'.format('Parallel run with n={}'.format(n)))
    t = timeit.Timer('parallel(n)', globals=globals())
    reps = 10
    print([i/reps for i in t.repeat(number=reps)])
