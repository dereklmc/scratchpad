import sys

def sieve(limit):
	is_prime = [False] * 2 + [True] * (limit - 1)
	for n in xrange(limit + 1):
		if is_prime[n]:
			yield n
			is_prime[n**2::n] = [False for i in xrange(n*n, limit+1, n)]

def main():
	a = list(sieve(int(sys.argv[1])))
	print "Number Primes: ", len(a)

if __name__ == '__main__':
	main()
