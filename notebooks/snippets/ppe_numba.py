@jit(nopython=True)
def pressure_poisson(p, b, l2_target=1e-3):
    pn = p.copy()
    J, I = b.shape

    iter_diff = l2_target + 1

    while iter_diff > l2_target:
        n = 0
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
            iter_diff = numpy.sqrt(numpy.sum((p - pn)**2)/numpy.sum(pn**2))
        if n == 500:
            break

        n += 1

    return p
