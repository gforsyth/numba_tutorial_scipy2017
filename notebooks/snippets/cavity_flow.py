def cavity_flow(nt, u, v, dt, dx, dy, p, rho, nu):
    un = numpy.empty_like(u)
    vn = numpy.empty_like(v)
    ny, nx = u.shape
    b = numpy.zeros((ny, nx))

    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        b = bracket_term_ppe(b, rho, dt, u, v, dx, dy)
        p = pressure_poisson(p, dx, dy, b, 1e-3)

        u[1:-1,1:-1] = (un[1:-1, 1:-1] -
                        un[1:-1,1:-1] * dt / dx *
                        (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                        vn[1:-1, 1:-1 ] * dt / dy *
                        (un[1:-1, 1:-1] - un[0:-2, 1:-1]) -
                        dt / (2 * rho * dx) *
                        (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                        nu * dt *
                        (1 / dx**2 *
                         (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                        1 / dy**2 *
                         (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

        v[1:-1,1:-1] = (vn[1:-1, 1:-1] -
                        un[1:-1, 1:-1] * dt / dx *
                        (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                        vn[1:-1, 1:-1] * dt / dy *
                        (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) -
                        dt / (2 * rho * dy) *
                        (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                        nu * dt *
                        (1 / dx**2 *
                         (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                        1 / dy**2 *
                         (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] +vn[0:-2, 1:-1])))

        #remember order of these will have a (very small) effect on the 
        #final answers.  if you want to compare between versions, make sure
        #they match up
        u[:, 0] = 0
        u[:, -1] = 0
        v[:, 0] = 0
        v[:, -1] = 0
        u[0, :] = 0
        u[-1, :] = 1    #set velocity on cavity lid equal to 1
        v[0, :] = 0
        v[-1, :]=0
        
        
        
    return u, v, p
