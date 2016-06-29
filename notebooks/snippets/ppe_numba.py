@jit(nopython=True)
def pressure_poisson(p, b, l2_target):
    I, J = b.shape

    iter_diff = l2_target + 1

    n = 0
    while iter_diff > l2_target and n <= 500:
        pn = p.copy()
        for i in range(1, I - 1):
            for j in range(1, J - 1):
                p[i, j] = (.25 * (pn[i, j + 1] +
                                  pn[i, j - 1] +
                                  pn[i + 1, j] +
                                  pn[i - 1, j]) -
                                  b[i, j])

        for i in range(I):
            p[i, 0] = p[i, 1]
            p[i, -1] = 0

        for j in range(J):
            p[0, j] = p[1, j]
            p[-1, j] = p[-2, j]

        if n % 10 == 0:
            iter_diff = numpy.sqrt(numpy.sum((p - pn)**2)/numpy.sum(pn**2))

        n += 1

    return p
