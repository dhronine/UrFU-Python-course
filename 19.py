import datetime

def findFirstandSundays():
	result = sum(1
		for i in range(1901, 2001)
		for f in range(1, 13)
		if datetime.date(i, f, 1).weekday() == 6)
	return str(result)

print(findFirstandSundays())
    
input('Press ENTER to exit')