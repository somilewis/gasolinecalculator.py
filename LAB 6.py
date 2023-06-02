# Lewis Muthomi
# 1250 01
# 9/26/22
# lab 6

# This program will calculate the cost of gasoline for a trip.
# You will need to know your cars MPG,whatyou paid for a gallon
# of gas, and the distance  in miles you travelled.

# User greeting
print('Welcome to calculate gasoline cost for a trip')
print()

# Take user input
distanceMiles = float(input('Please enter the distance you travelled in miles: '))
mpg = float(input('Enter the Miles per Gallon for this trip: '))
cost = float(input('Enter the cost per Gallon paid: '))
print()

# Do math
answer = distanceMiles / mpg * cost

# Display results 
print('The cost for this trip is/was: $',format(answer,',.2f'))

# Exit message
print()
print('Have a nice day!!!')
