
def decorator_func(function):
	def wrapper(x,y):
		if x <= 0 or y <= 0:
			return "Xatolik"
		else:
			return function(x,y)
	return wrapper		
			

@decorator_func
def func(x,y):
	return x + y

print(func(4,5))