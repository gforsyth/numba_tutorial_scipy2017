@guvectorize(['float64[:], float64[:], float64[:]'], '(n),(m)->(m)')
def return_half_array(in_array, out_array2, out_array):
    for i in range(in_array.shape[0] // 2):
        out_array[i] = in_array[i]

in_array = numpy.arange(20)
out_array = numpy.empty(10)

return_half_array(in_array, out_array, out_array)
