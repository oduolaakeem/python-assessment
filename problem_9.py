"""
	Problem 9
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a2 + b2 = c2
	For example, 32 + 42 = 9 + 16 = 25 = 52.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

def special_pythgorean_triplet(total):
	for a in range(1,total + 1):
		for b in range(a+1,total+1):
			c = total - a - b
			if a ** 2 + b ** 2 == c ** 2:
				return a * b * c

if __name__ == "__main__":
    print(special_pythgorean_triplet(1000))