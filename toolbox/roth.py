# Roth IRA value benchmark
# calculates the expected value of a Roth IRA <yrs> years since opening
# NB: this program assumes constant maximum annual contribution ($6000.00)

# output: <yrs> <tsm> <value>
#  yrs: years since initial investment, same as input
#  tsm: total sum multiplier, the factor by which the total contribution has grown by
#   NB: this is less than the growth of the first contribution, 1.1^n
#  value: the projected/expected value of the IRA account after <yrs>


roi = 1.1
time = int(input("Years in market: "))
def project(yrs):
	factor = (1. - roi ** (yrs + 1))/(1. - roi) - 1
	print(yrs, round((factor/yrs), 3), round(6000. * factor, 2))

project(time)

