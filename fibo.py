# Fibonacci series using recursion 
def fib(n): # write Fibonacci series up to n
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

def fib2(n): # return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result
