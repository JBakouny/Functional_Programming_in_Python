
def mapReduce(zero, reducer, mapper, a, b) :
    res = zero
    for i in range(a, b + 1) :
        res = reducer(res, mapper(i))
    return res

def product (f, a, b) :
    return mapReduce(1, lambda x, y : x * y, f, a, b)

def sum (f, a, b) :
    return mapReduce(0, lambda x, y : x + y, f, a, b)

def sumInts (a, b) :
    return sum(lambda x : x, a, b)

def sumCube (a, b) :
    return sum(lambda x : x**3, a, b)

def fact(n) :
    return product(lambda x : x, 1, n)

def sumFact (a, b) :
    return sum(fact, a, b)
