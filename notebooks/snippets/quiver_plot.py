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
