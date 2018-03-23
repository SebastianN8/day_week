#
# day_week.py
#
# Created by: Sebastian N
# Created on: March 23
#
# This program determines if the day is part of the weekend or the week
#

# Function
def what_day_is(day_passed_in):
	# If statement 
	if day_passed_in == 'Saturday' or day_passed_in == 'Sunday':
		print('Yay! It is day of the weekend.')
	elif day_passed_in in my_week_days:
		print('Oh no! You are on a week day.')
	else:
		print('Your input is not valid!')

# Variables
my_week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_week = input('What day is it today: ')

# Calling function
result = what_day_is(day_week)
input()