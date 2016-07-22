"""
	Factorial digit sum
	Problem 20
	n! means n × (n − 1) × ... × 3 × 2 × 1
	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
	Find the sum of the digits in the number 100!
"""
import math

def factorial_digit_sum(number):
	digits_sum = sum(int(c) for c in str(math.factorial(number)))
	return digits_sum

if __name__ == "__main__":
    print(factorial_digit_sum(100))