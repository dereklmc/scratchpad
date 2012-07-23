def condition(p, q):
    if p and not q:
        return False
    return True

def bicondition(p, q):
    return p is q

def s1(p,q):
    return condition(p and q, p)

def s2(p,q):
    return bicondition(p, not (p or q))

def s3(p,q):
    return bicondition(p and q, p or q)

statements = [s1, s2, s3]

bools = [True, False]

for s in statements:
    for i in bools:
        for j in bools:
            print "%s\t%s\t-\t%s" % (i,j,s(i,j))
    print "\n\n"

