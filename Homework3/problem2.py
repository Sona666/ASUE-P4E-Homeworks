def PrimeNumbers(value):
	primes = []
	
	if value > 1:
		for i in range(2,value+1):
			prime = True
			for j in range(2,i):
				if i % j ==0 :
					prime = False
			if prime:
				primes.append(i)
	return(primes)
print(PrimeNumbers(5))
