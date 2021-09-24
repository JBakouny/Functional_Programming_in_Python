
def mapReduce(zero, reducer, mapper, a, b) :
    res = zero
    for i in range(a, b + 1) :
        res = reducer(res, mapper(i))
    return res

def product(f) :
    def res(a, b) :
        return mapReduce(1, lambda x, y : x * y, f, a, b)
    return res

def sum (f) :
    def res(a, b):
        return mapReduce(0, lambda x, y : x + y, f, a, b)
    return res

sumInts = sum(lambda x : x)
sumCube = sum(lambda x : x**3)

def fact(n) :
    return product(lambda x : x)(1, n)

sumFact = sum(fact)
