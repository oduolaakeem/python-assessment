import math, itertools

def highly_divisible_triangular_number(limit):
	triangle = 0
	for i in itertools.count(1):
		triangle += i  # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
		if num_divisors(triangle) > limit:
			break
	return str(triangle)


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
	result = 0
	end = int(math.sqrt(n))
	for i in range(1, end + 1):
		if n % i == 0:
			result += 2
	if end**2 == n:
		result -= 1
	return result


if __name__ == "__main__":
	print(highly_divisible_triangular_number(500))
