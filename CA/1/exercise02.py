# task :
#
# Exercise 2)
# Write a program to manipulate information within variables. Your program should:
# • Take in two numbers and store them in variables num1 and num2.
# • Swap the contents of the variables (so the value originally stored in num1 ends up in num2, and the value
# originally stored in num2 ends up in num1)
# • Display the contents of num1 and num2

# ask for two numbers and store them into variables
num1 = input('please enter a number ')
num2 = input('please enter second number ')

# swap variables via assigning two values to two variables at the same time
num1, num2 = num2, num1

# displaying the contents using funtion print
print('first number is', num1, 'second number id', num2)
