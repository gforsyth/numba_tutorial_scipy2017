@guvectorize(['float64[:,:], float64, float64, float64, int64, float64[:,:]'], 
            '(m,m),(),(),(),()->(m,m)', nopython=True)
def ftcs_loop(T, alpha, dt, dx, nt, Tn):
    I, J = T.shape
    for n in range(nt):
        for i in range(1, I - 1):
            for j in range(1, J - 1):
                Tn[i,j] = (T[i, j] + 
                          alpha * 
                          (dt/dx**2 * (T[i + 1, j] - 2*T[i, j] + T[i - 1, j]) + 
                           dt/dx**2 * (T[i, j + 1] - 2*T[i, j] + T[i, j - 1])))

        for i in range(I):
            Tn[i, 0] = T[i, 0]
            Tn[i, J - 1] = Tn[i, J - 2]

        for j in range(J):
            Tn[0, j] = T[0, j]
            Tn[I - 1, j] = Tn[I - 2, j]

        T = Tn.copy()