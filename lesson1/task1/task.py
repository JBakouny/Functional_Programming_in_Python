
def product (f, a, b) :
    if (a > b) :
        return 0
    else :
        return f(a) * sum(f, a + 1, b)


def sum (f, a, b) :
    if (a > b) :
        return 0
    else :
        return f(a) + sum(f, a + 1, b)

def sumInts (a, b) :
    return sum(lambda x : x, a, b)

def sumCube (a, b) :
    return sum(lambda x : x**3, a, b)

def fact(x) :
    if x == 0 :
        return 1
    return x * fact(x - 1)

def sumFact (a, b) :
    return sum(fact, a, b)

print(sumInts(5, 10))
print(sumCube(5, 10))
print(sumFact(5, 10))