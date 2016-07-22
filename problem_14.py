def longest_collatz_sequence(limit):
	result = max(range(1, limit), key=sequence_length)
	return str(result)


sequence_cache = {1: 1}

def sequence_length(x):
	if x not in sequence_cache:
		if x % 2 == 0:
			y = x // 2
		else:
			y = x * 3 + 1
		sequence_cache[x] = sequence_length(y) + 1
	return sequence_cache[x]


if __name__ == "__main__":
	print(longest_collatz_sequence(1000000))