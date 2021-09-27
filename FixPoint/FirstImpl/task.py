
def fixPoint(f):
    def isCloseEnough(x, y, precision=0.0000000000000000001):
        return abs((x - y) / x) < precision

    def iterate(guess):
        next = f(guess)
        while not isCloseEnough(guess, next) :
            next = f(next)
        return next

    return iterate(1.0)
