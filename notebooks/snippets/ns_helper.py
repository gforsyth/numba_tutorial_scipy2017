import numpy
from matplotlib import pyplot, cm

def cavity_flow(u, v, p, nt, dt, dx, velocity_term, pressure_poisson, rho=1, nu=0.1, rtol=1e-3):
    '''
    Solves the Navier-Stokes equations for a lid-driven cavity using
    finite-differences on a collocated grid in 2D

    Parameters
    ----------
    u : floats; discretized velocity in x-direction
    v : floats; discretized velocity in y-direction
    p : floats; discretized pressure field
    nt : int; number of timesteps to run
    dt : float; size of individual timestep
    dx : float; spacing of individual grid points
    rho : float; density
    nu : float; kinematic viscosity
    rtol : float; relative tolerance to solve between successive iterations
           in pressure_poisson solver
    '''

    un = numpy.empty_like(u)
    vn = numpy.empty_like(v)
    ny, nx = u.shape
    b = numpy.zeros((ny, nx))

    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        b = velocity_term(b, rho, dt, u, v, dx)
        p = pressure_poisson(p, b, rtol)

        u[1:-1,1:-1] = (un[1:-1, 1:-1] - dt / dx *
                        (un[1:-1,1:-1] * (un[1:-1, 1:-1] -
                                          un[1:-1, :-2]) +
                        vn[1:-1, 1:-1 ] * (un[1:-1, 1:-1] -
                                            un[:-2, 1:-1]) +
                        1 / (2 * rho) * (p[1:-1, 2:] -
                                         p[1:-1, :-2])) +
                          nu * dt / dx**2 *
                         (un[1:-1, 2:] +
                          un[1:-1, :-2] +
                          un[2:, 1:-1] +
                          un[:-2, 1:-1] -
                          4 * un[1:-1, 1:-1]))

        v[1:-1,1:-1] = (vn[1:-1, 1:-1] - dt / dx *
                        (un[1:-1,1:-1] * (vn[1:-1, 1:-1] -
                                          vn[1:-1, :-2]) +
                         vn[1:-1, 1:-1 ] * (vn[1:-1, 1:-1] -
                                            vn[:-2, 1:-1]) +
                        1 / (2 * rho) * (p[2:, 1:-1] -
                                         p[:-2, 1:-1])) +
                        nu * dt / dx**2 *
                         (vn[1:-1, 2:] +
                          vn[1:-1, :-2] +
                          vn[2:, 1:-1] +
                          vn[:-2, 1:-1] -
                          4 * vn[1:-1, 1:-1]))

        u[:, 0] = 0
        u[:, -1] = 0
        v[:, 0] = 0
        v[:, -1] = 0
        u[0, :] = 0
        u[-1, :] = 1    #set velocity on cavity lid equal to 1
        v[0, :] = 0
        v[-1, :] = 0

    return u, v, p


def quiver_plot(u, v, p, nx=41):
    nx = 41
    ny = nx
    x = numpy.linspace(0, 2, nx)
    y = numpy.linspace(0, 2, ny)
    X, Y = numpy.meshgrid(x, y)

    quiver_skip = qs = 4
    pyplot.figure(figsize=(11, 7), dpi=100)
    pyplot.contourf(X, Y, p, alpha=0.5, cmap=cm.viridis)
    pyplot.colorbar()
    pyplot.contour(X, Y, p)
    pyplot.quiver(X[::qs, ::qs], Y[::qs, ::qs], u[::qs, ::qs], v[::qs, ::qs])
    pyplot.xlabel('$x$', fontsize=18)
    pyplot.ylabel('$y$', fontsize=18)
