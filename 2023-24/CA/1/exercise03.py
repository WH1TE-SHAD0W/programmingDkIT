# task :
#
# Exercise 3)
# Write a program to calculate a bill based on if the user is a member of the company scheme. If the user is a
# member, the rate for the service is €5 per hour. If they are not a member, the rate is €10 per hour. Your program
# should:
# • Ask the user how many hours they used the service for.
# • Check if the user is a member of the scheme.
# • Calculate the appropriate service bill (non-members pay €10 per hour, members pay €5 per hour)
# • Calculate the tax (non-members pay 20% tax, members pay 10%)
# • Calculate and displays the final bill total.

# get info of service usage in hours
hours_used_service: int = int(input('please write down number of hours you used the gym '))

# get info of membership
membership: str = str(input('do you have active membership? if so write down "yes", otherwise "no" '))

# prevent final bill calculation without values of tax and service bill which can be not calculated when the membership
# information is misspelled, that can be done by implementing default value in match statement or
# using else in if statement


# calculation of the service bill based on membership
if membership == 'yes':
    service_bill: float = hours_used_service * 5
elif membership == "no":
    service_bill: float = hours_used_service * 10
else:
    service_bill: int = 0
# calculation of the tax based on membership
if membership == 'yes':
    tax: float = hours_used_service * 0.1
elif membership == "no":
    tax: float = hours_used_service * 0.2
else:
    tax: int = 0

# calculate the final bill and display it via print, it's just a difference of tax and bill pay
print('final bill is', service_bill - tax, '€')
