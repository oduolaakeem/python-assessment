"""
	Largest prime factor
	Problem 3
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
"""

import math

def is_prime(n):
    if (n <= 1) or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def largest_prime_factor(number):
	prime_factors = []
	for i in range(2, int(math.sqrt(number) + 1)):
	    if number % i == 0:
	    	prime_factors.append(i)
	    	number = number // i
	    	if is_prime(number):
	    		prime_factors.append(number)
	    		break;
	largest_prime = prime_factors.pop()
	return largest_prime

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))