cache = {}

def factorial(n):
	if n == 0:
		return 1
	if n in cache:
		return cache[n]
	cache[n] = n * factorial(n)
	return cache[n]

while True:
	i = input('Enter an integer: ' )
        if  i == 'exit':
		break
	print(factorial(int (i)))	      
