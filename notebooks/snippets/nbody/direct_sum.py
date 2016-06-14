@njit
def direct_sum(particles):
    for i, target in enumerate(particles):
        for j, source in enumerate(particles):
            if i != j:
                r = distance(target, source)
                target.phi += source.m / r
                
    return particles
