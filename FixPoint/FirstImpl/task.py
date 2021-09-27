
def fixPoint(f):
    def isCloseEnough(x, y, precision=0.0000000000000000001):
        return abs((x - y) / x) < precision

    next = f(1.0)
    while not isCloseEnough(f(next), next) :
        next = f(next)
    return next

def averageDamp(f):
    def res(x) :
        return (x + f(x)) / 2
    return res

def sqrt(x) :
    return fixPoint(averageDamp(lambda y : x / y))