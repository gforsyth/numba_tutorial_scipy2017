@guvectorize(['(int16[:,:], int16[:], int16[:,:])',
              '(float32[:,:], float32[:], float32[:,:])',
              '(float64[:,:], float64[:], float64[:,:])'], '(n,n),(m)->(m,m)')
def interpolate_2d_gvec(coarse, size, fine):
    I, J = coarse.shape
    for i in range(0, I - 1):
        for j in range(0, J - 1):
            fine[2 * i, 2 * j] = coarse[i, j]
            fine[2 * i + 1, 2 * j] = .5 * (coarse[i, j] +
                                            coarse[i + 1, j])
            fine[2 * i, 2 * j + 1] = .5 * (coarse[i, j] +
                                            coarse[i, j + 1])
            fine[2 * i + 1, 2 * j + 1] = .25 * (coarse[i, j] +
                                                coarse[i + 1, j] +
                                                coarse[i, j + 1] +
                                                coarse[i + 1, j + 1])

        fine[2 * i, 2 * (J - 1)] = coarse[i, (J - 1)]
        fine[2 * i + 1, 2 * (J - 1)] = .5 * (coarse[i, J - 1] +
                                            coarse[i + 1, J - 1])
    for j in range(0, J):
        fine[2 * (I - 1), 2 * j] = coarse[(I - 1), j]
        fine[2 * (I - 1), 2 * j + 1] = .5 * (coarse[I - 1, j] +
                                    coarse[I - 1, j + 1])
