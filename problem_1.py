"""
	Multiples of 3 and 5
	Problem 1
	If we list all the natural numbers below 10 that are multiples of 3 or 5, 
	we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
	Solution: 
	- Iterate through the list of numbers
	- Check divisibility by 3 or 5
	- Add number(s) if divisibility is true
"""

def sum_of_multiples_of_3_or_5_below(number):
	answer = sum(x for x in range(1,number) if (x % 3 == 0 or x % 5 == 0))
	
	return answer

if __name__ == "__main__":
    print(sum_of_multiples_of_3_or_5_below(1000))