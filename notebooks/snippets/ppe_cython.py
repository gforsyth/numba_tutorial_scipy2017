%%cython
cimport numpy
cimport cython

import numpy

from libc.math cimport sqrt

@cython.boundscheck(False)
def pressure_poisson(numpy.ndarray[numpy.float_t, ndim=2] p,
                     numpy.ndarray[numpy.float_t, ndim=2] b,
                     double l2_target):

    cdef numpy.ndarray[numpy.float_t, ndim=2] pn = numpy.zeros_like(p)
    cdef int j, i, n
    cdef double iter_diff
    cdef int J = b.shape[0]
    cdef int I = b.shape[1]

    iter_diff = l2_target + 1

    n = 0
    while iter_diff > l2_target:
        pn = p.copy()
        for j in range(1, J - 1):
            for i in range(1, I - 1):
                p[j, i] = (.25 * (pn[j, i + 1] +
                                  pn[j, i - 1] +
                                  pn[j + 1, i] +
                                  pn[j - 1, i]) -
                                  b[j, i])

        for j in range(J):
            p[j, 0] = p[j, 1]
            p[j, -1] = p[j, -2]

        for i in range(I):
            p[0, i] = p[1, i]
            p[-1, i] = 0

        if n % 10 == 0:
            iter_diff = L2_Cython(p, pn)
        if n == 500:
            break
        n += 1

    return p


@cython.boundscheck(False)
def L2_Cython(numpy.ndarray[numpy.float_t, ndim=2] p,
              numpy.ndarray[numpy.float_t, ndim=2] pn):
    cdef double error = 0
    cdef double pnsum = 0
    cdef int ny = p.shape[0]
    cdef int nx = p.shape[1]
    for i in range(nx):
        for j in range(ny):
            error += (p[i,j]-pn[i,j])**2
            pnsum += pn[i,j]**2

    return sqrt(error/pnsum)
