x = int(input("enter min number"))
y = int(input("entyer max number"))
i = x
if i % 2 ==0:
	i = x+1
	while i <=y:
		print(i)
		i+=2