import numpy
from time import sleep

def bad_call(dude):
    sleep(.5)
 
def worse_call(dude):
    sleep(1)
 
def sumulate(foo):
    if not isinstance(foo, int):
        return
 
    a = numpy.random.random((1000, 1000))
    a @ a
    ans = 0
    for i in range(foo):
        ans += i
 
    bad_call(ans)
    worse_call(ans)
 
    return ans

if __name__ == '__main__':
    sumulate(15)
