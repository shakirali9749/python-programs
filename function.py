
def do_something(*args):
	print(f'{args} called this method!')
	

# do_something('Ali Adnan', 30)

# do_something('Umar Ali')


name = ("shakir",23)
print(name[1])



# do_something()

def profile(firstname, lastname='Fielding',*args,**kwargs):
	full_name = f'{firstname} {lastname}'
	print(kwargs)
	print(args)

	return full_name.title()

# profile = profile("feilding","roy")

# print(profile)


# print(profile(lastname='fielding', firstname='roy'))

# print(profile('fielding', 'roy', 45,90,100,'source code', age=40, degree='phd'))

# print(profile('Roy'))

# print(profile('Thomas', 'Roy'))

# print(profile('Amjad'))


# def value_inspector(n):
# 	n[2] = 'new code'
# 	print(n)

# m = [12,14,'source code']
# value_inspector(m)
# print(m)
