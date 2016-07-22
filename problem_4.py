def is_palindrome(number):
	number_str = str(number)

	if number_str == number_str[::-1]:
		return True
	else:
		return False

def palindrome(num_digit):
	i = "1" + ("0"*num_digit)
	product = 1
	for j in range(1,int(i)):
		for k in range(j,int(i)):
			temp_product = j * k 
			if is_palindrome(temp_product):
				if temp_product > product:
					product = temp_product
	return product

if __name__ == "__main__":
    print(palindrome(3))