
def mapReduce(zero, reducer, mapper, a, b) :
    if a > b :
        return zero
    else :
        return mapReduce(reducer(mapper(a), zero), reducer, mapper, a + 1, b)

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
