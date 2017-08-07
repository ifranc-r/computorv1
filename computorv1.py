from math import *
from time import sleep
import sys

def is_num(num):
    try:
        float(num) # for int, long and float
    except ValueError:
    	print "\nError:\nThe input are not correct\n"
    	sys.exit(-1)
    return float(num)


def	solvequadratic(a, b, c):

	discriminant = b * b - 4 * a * c

	if (discriminant < 0):
		print "The discriminant is negative\nThere is no solution\n"
		return (0)
	elif (discriminant == 0):
		x1 = -0.5 * b / a
		print "The discriminant is 0, The one solution is\n %.2f \n" % (x1)
		return 1
	elif (discriminant >= 0):
		discriminant = sqrt(discriminant)
		x1 = ((-b + discriminant) / (2 * a))
		x2 = ((-b - discriminant) / (2 * a))
		print "The discriminant is positive,\nThe two solution are :\n > %.2f \n > %.2f\n" % (x1, x2)
		return 2
def solvepolynomial(a, b):
	if (b >= a):
		return  (b / a)
	if (b < a):
		return  -(b / a)

#def noDiscr(*x):
#	print "Or it's invalid or there is no solution\n"
#def oneDiscr(*x):
#	print "The one solution is\n %.2f \n" % (x[0])
#def twoDiscr(*x):
#	print "The two solution are :\n > %.2f \n >>%.2f\n" % (x[0], x[1])
#options = {0 : noDiscr,
#           1 : oneDiscr,
#           2 : twoDiscr 
#}

def main():
	option = is_num(raw_input("Chose your Polynomial Degree (1 to 2)?\n"))
	if (option == 2):
		print "ax^2 + bx + c = 0 \n"
		a = is_num(raw_input("Chose the value of \'a\' ?\n"))
		b = is_num(raw_input("Chose the value of \'b\' ?\n"))
		c = is_num(raw_input("Chose the value of \'c\' ?\n"))
		sleep(1)
		print "\nThe equation is : (%.2f * x^2) + (%.2f * x) + %.2f = 0\n" % (a, b, c)
		sleep(2)
		solvequadratic(a, b, c)
	elif (option == 1):
		print "ax + b = 0 \n"
		a = is_num(raw_input("Chose the value of \'a\' ?\n"))
		b = is_num(raw_input("Chose the value of \'b\' ?\n"))
		sleep(1)
		print "\nThe equation is : (%.2f * x) + %.2f = 0\n" % (a, b)
		sleep(2)
		print "\nthe solution is %.2f \n" % (solvepolynomial(a, b))
	else:
		print " It has to be a number betwen 1 and 2\n"
		sys.exit(0)
main()



