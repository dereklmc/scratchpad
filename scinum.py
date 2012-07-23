class ScientificNum(object):
    
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
    
    def __str__(self):
        return "{0}E{1}".format(self.base, self.exponent)
    
    def __pow__(self, other):
        return ScientificNum(self.base**other, self.exponent*other)
    
    def __rpow__(self, other):
        return other**self.toDecimal()
    
    def __mul__(self, other):
        if isinstance(other, ScientificNum):
            newBase = self.base * other.base
            newExponent = self.exponent + other.exponent
            return ScientificNum.fromDecimal(newBase, newExponent)
        else:
            newBase = self.base * other
            return ScientificNum.fromDecimal(newBase, self.exponent)
    
    def __rmul__(self, other):
        return other*self.toDecimal()
    
    def __add__(self, other):
        if !isinstance(other, ScientificNum):
            other = ScientificNum.fromDecimal()
        newExponent = max(self.exponent, other.exponent)
        while 
    
    def __int__(self):
        return self.toDecimal()
        
    def __long__(self):
        return self.toDecimal()
    
    def toDecimal(self):
        return self.base * 10**self.exponent
    
    @classmethod
    def fromDecimal(cls, num, baseExponent = 0):
        exponent = baseExponent
        while num >= 10.0:
            num /= 10.0
            exponent += 1
        while num < 1.0:
            num *= 10.0
            exponent -=1
        return ScientificNum(num, exponent)

def foo(x):
    return abs(x)**0.5 + x**3 * 5

a = ScientificNum(2,0)
b = ScientificNum(2,2)
c = ScientificNum(1,1)
d = ScientificNum(3,0)

print "a", a, int(a)
print "b", b, int(b)
print "c", c, int(c)
print "d", d, int(d)

print "a**2 = "

test = a**2

print test

print "2**a = "

test = 2**a

print test

print "c**a = "

test = c**a

print test

print "2*d = "

test = 2 * d

print test

print "d*2 = "

test = d * 2

print test

print "a*d = "

test = a * d

print test


print "2+d = "

test = 2 + d

print test

print "d+2 = "

test = d + 2

print test

print "a+d = "

test = a + d

print test
