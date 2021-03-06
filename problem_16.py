"""
	Power digit sum
	Problem 16
	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2^1000?
"""
def power_digit_sum(power):
	digits_sum = sum(int(c) for c in str(2**power))
	return digits_sum

if __name__ == "__main__":
    print(power_digit_sum(1000))

