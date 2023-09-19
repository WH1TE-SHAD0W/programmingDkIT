'''#take first name from user
fName: str = input('please write your first name')
#take last name from user
lName: str = input('please write your last name')
#create full name
full_name: str = fName + lName

#display full name
print(full_name)'''

'''#working with numbers
num1: int = int(input('enter your first number'))
num2: int = int(input('enter your second number'))
total: int = num1 + num2
print('Your total is:', total)'''


'''
#exercise 9


jogging: int = int(input('how much hours did you jog?'))
cycling: int = int(input('how much hours did you cycle?'))
swimming: int = int(input('how much hours did you swim?'))

calories_table: dict = {'jog' : 475, 'cycle' : 200, 'swim' : 275}

total_calories: int = jogging * calories_table['jog'] + cycling * calories_table['cycle'] + swimming * calories_table['swim']

weight_loss: float = total_calories / 3500

print('you lost', weight_loss, 'pounds')
'''
'''
#exercise 8

hours: int = int(input())
minutes: int = int(input())
seconds: int = int(input())

total_seconds: int = hours * 3600 + minutes * 60 + seconds

print('you exercised', total_seconds , 'seconds')
'''
'''
#exercise 7
temperature_farenheit: int = int(input('what temperature it is right now in farenheit?'))
temperature_celsius: float =  float((5/9)*(temperature_farenheit -32)
)
print('it is' , temperature_celsius, 'right now in celsius' )

'''
'''
#exercise 6

acres_of_farmland: int = int(input('write the are of your farmland in acres'))
print('your farmland will produce' , acres_of_farmland * 18, 'of tons of corn')
'''
'''
#exercise 5
allems: int = int(input('input a number of allems'))
zoobies: float = allems / 0.028
print('the zoobies are' , zoobies)
'''
'''
# exercise  4
retail_price: float = float(input())
discount_recommended: float = float(input())
new_price = retail_price * ((100 - discount_recommended) / 100)
print('your new price with recommended price is', new_price)
'''
'''
# exercise 3
money_got = float(input())
money_spent = float(input())
money_earned = float(input())

print('after all you got', money_got - money_spent + money_earned)
'''










