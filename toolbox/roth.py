roi = 1.1
years = int(input("time in the market: "))
def project(yrs):
	factor = (1. - roi ** (yrs + 1))/(1. - roi) - 1
	# print('y' + str(yrs), 'x' + str(round((factor/yrs), 2)), '$' + str(round(6000. * factor, 2)))
	print('(' + str(yrs) + ',' + str(round((factor/yrs), 2)) + ')')

#for i in [-5, -3, -1, 0, 1, 3, 5]:
#	project(years + i)

for i in range(2, 65):
	project(i)
