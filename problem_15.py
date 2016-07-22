import math

def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))


def number_of_routes(grid):
	result = nCr(2*grid, grid)
	return result

if __name__ == "__main__":
    print(number_of_routes(20))
