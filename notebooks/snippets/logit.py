@vectorize([float64(float64)])
def logit(a):
    return math.log(a / (1 - a))

a = numpy.linspace(.1, .9, 9)
