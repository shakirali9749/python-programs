def doSomething(*arguments):
	print(f'{arguments[0]} called this method')
	print(f'{arguments[1]} is {arguments[0]}`s age')



# doSomething("shakir",78)


number = 0
active = True

while active:
	print(number)
	number = number + 1
	if number > 70:
		active = False


