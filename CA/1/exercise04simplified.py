# task :
#
# Exercise 4)
# Write a program to print out a message to a student based on their grade average. Your program should:
# • Take in the grade received in three different subjects (Maths, History and Geography). The allowable
# range on these grades is 0 to 100. If one or more of the grades entered are not within the allowable range
# of values, the program should print a message indicating the grade is impossible. It should not carry out
# the remainder of the program’s logic.
# • Calculate the average of the three grades
# • Display the following messages:
# o For an average of 70% or higher, display “Your GPA was X, well done!”
# o For an average of 40% to 69%, display “Your GPA was X, good effort, but keep working”
# o For an average of below 40%, display “Your GPA was X, maybe see if you can study with a
# classmate?”

# asking for a grade from math
grade_math = int(input('please enter a grade for maths in the range from 0 to 100'))
# asking for a grade from geography and storing it in a variable
grade_geography = int(input('please enter a grade for geography in the range from 0 to 100'))
# asking for a grade from history stored in variable
grade_history = int(input('please enter a grade for history in the range from 0 to 100'))

# in all these if statements I am checking if all these grades are valid
if 0 <= grade_math <= 100 and 0 <= grade_geography <= 100 and 0 <= grade_history <= 100:
    # calculating the average of all these grades
    average = (grade_history + grade_geography + grade_math) / 3
    # if the average is higher than 70 it displays the value and says well done
    if 70 >= average:
        print('Your GPA was', average, ', well done!')
    # if the value is in between 40 and 70 it says another expression
    elif 40 >= average < 70:
        print('Your GPA was', average, ', good effort, but keep working')
    # if the value is below 40 it says another expression that the student should study more
    elif average < 40:
        print('Your GPA was', average, ', maybe see if you can study with a classmate?')

# all these else statements are to bypass all the logic when any of the grade values are not met
# in the range of acceptable
else:
    print('the grade you put in is impossible')

