def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-1)+fib(n-2)
#try:
#	n=int(input("enter num"))
#except ValueError:
#	print(value is not positive)
#if(n>=1):
	for i in range(20):
		print (fib(i))
