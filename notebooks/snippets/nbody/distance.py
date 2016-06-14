@njit
def distance(part1, part2):
    '''calculate the distance between two particles'''
    return ((part1.x - part2.x)**2 + 
            (part1.y - part2.y)**2 + 
            (part1.z - part2.z)**2)**.5
