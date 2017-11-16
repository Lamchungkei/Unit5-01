# Created by: Kay Lin
# Created on: 13th-Nov-2017
# Created for: ICS3U
# This program displays that generates 10 random numbers 
# between 1 and 100
# and calculate the average

from numpy import random

my_numbers = []

def average(my_numbers):
    # generate 10 random numbers and calculate the average
    print('There are 10 random numbers')
    
    for number in range(10):
        my_numbers.append(random.randint(1,100))
        print (my_numbers[number])

    #calculate the average
    average = sum(my_numbers)/int(len(my_numbers))
    return average

result = average(my_numbers)
print ('The average of random numbers is ' + str(result))
