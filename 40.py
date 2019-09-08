def FindTheValue():
	string = "".join(str(i) for i in range(1, 1000000))
	answer = 1
	for i in range(7):
		answer *= int(string[10**i - 1])
	return str(answer)

print(FindTheValue())
    
input('Press ENTER to exit')