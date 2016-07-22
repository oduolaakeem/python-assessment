"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

import math

def is_prime(n):
    if (n <= 1) or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def prime_number(limit):
	count = 0
	for x in range(1,100**100):
		if is_prime(x):
			count += 1
		if count == limit:
			return x
			break

if __name__ == "__main__":
    print(prime_number(10001))