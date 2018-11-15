value = int(input("Enter value: ")) 
if value > 1:
	for i in range(2,value):
		prime = True
		for j in range(2,i):
			if i % j ==0 :
				prime = False
		if prime:
			print(i)			


