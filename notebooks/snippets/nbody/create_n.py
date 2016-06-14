@njit
def create_n_random_particles(n, m, domain=1):
    '''
    Creates `n` particles with mass `m` with random coordinates
    between 0 and `domain`
    '''
    parts = numpy.zeros((n), dtype=particle_dtype)
    #attribute access only in @jitted function
    for i in parts:
        i.x = numpy.random.random() * domain 
        i.y = numpy.random.random() * domain
        i.z = numpy.random.random() * domain
        i.m = m
        i.phi = 0
    return parts
