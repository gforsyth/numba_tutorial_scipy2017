@guvectorize(['(int16[:,:], int16[:], int16[:,:])',
              '(int32[:,:], int32[:], int32[:,:])',
              '(float32[:,:], float32[:], float32[:,:])',
              '(float64[:,:], float64[:], float64[:,:])'], '(n,n),(m)->(m,m)')
def restrict_2d_gvec(fine, size, coarse):
    I, J = coarse.shape
    for i in range(1, I - 1):
        for j in range(1, J - 1):
            coarse[i, j] = (
                    1/16 * (
                    fine[2 * i - 1, 2 * j - 1] +
                    fine[2 * i - 1, 2 * j + 1] +
                    fine[2 * i + 1, 2 * j - 1] +
                    fine[2 * i + 1, 2 * j + 1]) +

                    1/8 * (
                    fine[2 * i, 2 * j - 1] +
                    fine[2 * i, 2 * j + 1] +
                    fine[2 * i - 1, 2 * j] +
                    fine[2 * i + 1, 2 * j]) +

                    1/4 * fine[i, j])

    for i in range(I):
        coarse[i, 0] = fine[2 * i, 0]
        coarse[i, -1] = fine[2 * i, -1]

    for j in range(J):
        coarse[0, j] = fine[0, 2 * j]
        coarse[-1, j] = fine[-1, 2 * j]
