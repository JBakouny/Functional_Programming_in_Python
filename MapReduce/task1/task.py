
def mapReduce(zero, reducer) :
    def helper1 (mapper):
        def helper2 (a , b) :
            res = zero
            for i in range(a, b + 1) :
                res = reducer(res, mapper(i))
            return res
        return helper2
    return helper1

product = mapReduce(1, lambda x, y : x * y)
sum = mapReduce(0, lambda x, y : x + y)
sumInts = sum(lambda x : x)
sumCube = sum(lambda x : x**3)

def fact(n) :
    return product(lambda x : x)(1, n)

sumFact = sum(fact)
