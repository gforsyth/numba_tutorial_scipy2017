def truncate(a, amin, amax):
    if a < amin:
        a = amin
    elif a > amax:
        a = amax
    return a

vec_truncate_serial = vectorize(['float64(float64, float64, float64)'])(truncate)
vec_truncate_par = vectorize(['float64(float64, float64, float64)'], target='parallel')(truncate)
