#TASK

#Implement the program to calculate common divisors from Lecture 16. You may use the solution on
#Pages 14–17 of the slides in your solution.

#PSEUDOCODE
#function findDivisors(num1, num2)
    #initialise divisors
        #for i from 1 to minmum(num1, num2) do
        #if num1 mod i == 0 and num2 mod i == 0 then
            #add i to divisors
    #return divisors

#Prompt the user for two positive integers
#if the numbers entered are not positive then
    #print out an error message
#else
    #find the common divisors
    #print out the common divisors
    #sum the common divisors
    #print out the total

# Program to get the common divisors of two positive integers supplied by the user
# Demonstrates the use of tuples

def findDivisors(num1, num2):
    """Finds the common divisors of num1 and num2
Assumes that num1 and num2 are positive integers
Returns a tuple containing the common divisors of num1 and num2"""
    divisors = ()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

number1 = int(input('Enter a positive integer: '))
number2 = int(input('Enter another positive integer: '))
if number1 <= 0 or number2 <= 0:
    print('Numbers should be > 0.')
else:
# First of all, get the common divisors and print them out
    divisors = findDivisors(number1, number2)
    print('The common divisors of', number1, 'and', number2, 'are:', divisors)
# Now sum them and print the total
    total = 0
    for d in divisors:
        total += d
    print('Sum of the common divisors is:', total)
print('Finished!')