# Task :
#
# Exercise 1)
# Write a program to calculate a user’s net pay for a month. Your program should:
# • Take in the user’s salary per hour and the number of hours worked in the last month
# • Calculate the gross pay for the user (and display it)
# • Calculate the taxes due on this pay, assuming the user’s tax rate is 42% (and display it)
# • Calculate the final net pay due to the user (and display it)


# prompts a statement to enter salary per hour, this float value is stored in a variable called 'user_salary_per_hour'
# which is also cast to prevent misuse of variable types
user_salary_per_hour: float = float(input("Please, enter your salary per hour "))

# it prompts a statement for the user to enter hours he works per month
hours_per_month: int = int(input('Please, enter you hours per month you worked '))

# the gross pay is just calculated by multiplication of hours worked per month and salary for each hour
gross_pay: float = user_salary_per_hour * hours_per_month

# round the value of gross pay into two decimal numbers
gross_pay = round(gross_pay, 2)

# let's just store the tax in a variable, so it can be referenced for any other usage
tax_rate: int = 42

# while the tax rate is 42%, we calculate it just by a simple multiplication representing this expression:
# value = base * percentage / 100, so it is going to be tax = gross_pay * 42 / 100
tax = gross_pay * tax_rate / 100

# round the value of tax into two decimal numbers
tax = round(tax, 2)

# show the tax to user
print('Your tax is', tax, "€")

# final net pay is just a difference of gross pay and tax, we can also display it to user directly and also round the
# value to two decimal digits
print('Your net pay is', round(gross_pay - tax, 2), '€')
