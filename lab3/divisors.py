def divisors():
	print("please enter a number")	
	n=int(input())
	i=0
	while (i<n+1):
		if(n%i==0):
			print(i)
	i+=1
divisors()
