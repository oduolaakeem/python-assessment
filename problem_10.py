"""
	Problem 10
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
"""
import math

def is_prime(n):
    if (n <= 1) or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def sum_of_primes_below(limit):
	sum_of_primes = 0
	for x in range(limit):
		if is_prime(x):
			sum_of_primes += x
	return sum_of_primes		

if __name__ == "__main__":
    print(sum_of_primes_below(2000000))