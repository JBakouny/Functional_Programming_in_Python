

def sqrt(x):
    def improve(guess):
        return (guess + x / guess) / 2

    def isGoodEnough(guess) :
        return abs((guess * guess - x) / x) < 0.001

    def sqrtIter(guess):
        if isGoodEnough(guess) :
            return guess
        else:
            return sqrtIter(improve(guess))

    return sqrtIter(1.0)

