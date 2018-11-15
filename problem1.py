list_ = list(map(int, input('Enter integers separated by spaces: ').split()))
min_ = list_[0]
max_ = list_[0]

for i in list_:
	if i < min_:
		min_=i
	elif i > max_:
		max_=i
diff = max_ - min_ 
print(diff)   


	 
