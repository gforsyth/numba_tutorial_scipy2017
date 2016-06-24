@guvectorize(['(int16[:,:], int16[:], int16[:,:])',
              '(float32[:,:], float32[:], float32[:,:])',
              '(float64[:,:], float64[:], float64[:,:])'], '(n,n),(m)->(m,m)')
def interpolate_2d_gvec(coarse, size, fine):
    I, J = coarse.shape
    for i in range(I):
        for j in range(J):
            fine[2 * i, 2 * j] = coarse[i, j]

    for i in range(I - 1):
        for j in range(J):
            fine[2 * i + 1, 2 * j] = .5 * (coarse[i, j] +
                                            coarse[i + 1, j])
    for i in range(I):
        for j in range(J - 1):
            fine[2 * i, 2 * j + 1] = .5 * (coarse[i, j] +
                                            coarse[i, j + 1])

    for i in range(I - 1):
        for j in range(J - 1):
             fine[2 * i + 1, 2 * j + 1] = .25 * (coarse[i, j] +
                                        coarse[i + 1, j] +
                                        coarse[i, j + 1] +
                                        coarse[i + 1, j + 1])
