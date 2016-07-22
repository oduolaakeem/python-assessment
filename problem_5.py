"""Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import math

def smallest_multiple(limit):
	ans = 1
	for i in range(1, limit+1):
		ans *= i // math.gcd(i, ans)
	return str(ans)

if __name__ == "__main__":
    print(smallest_multiple(20))