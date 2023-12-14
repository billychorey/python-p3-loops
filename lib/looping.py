#!/usr/bin/env python3
# using a while loop that outputs 
# numbers starting at 10 and counting 
# down to 1. After reaching 1, 
# print out "Happy New Year!"

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
        if i == 0:
            print("Happy New Year!")


# square_integers() that takes one argument, 
# a list of integers and 
# returns the list of squared elements.

def square_integers(int_list):
    squared_list = [num * num for num in int_list]
    return squared_list

# fizzbuzz() that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of 
# the number and for the multiples of five print 
# "Buzz". For numbers which are multiples of 
# both three and five, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

fizzbuzz()
