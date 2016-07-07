@njit
def create_n_random_particles(n, m, domain=1):
    '''
    Creates `n` particles with mass `m` with random coordinates
    between 0 and `domain`
    '''
    parts = numpy.zeros((n), dtype=particle_dtype)
    #attribute access only in @jitted function
    for p in parts:
        p.x = numpy.random.random() * domain
        p.y = numpy.random.random() * domain
        p.z = numpy.random.random() * domain
        p.m = m
        p.phi = 0
    return parts
