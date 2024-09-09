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

# creating a dictionary variable to store every mark in an array of a value of dictionary for each subject (key)
grades: dict = {'math': [], "history": [], "geography": []}

# getting the input every subject and inserting it into those arrays
for subject in grades:
    grades[subject] = input('please enter marks for ' + subject + 'please write them all in the following format: '
                                                                  'each separated by a space and the value must vary '
                                                                  'from 0 to 100').split(' ')
    # checking every number from input if is correct so continue if not quit the whole program
    for grade in grades[subject]:
        if int(grade) < 0 or int(grade) > 100:
            quit('you put a wrong value of a mark')
        else:
            pass

# setting up the dictionary variable to store average grades
average: dict = {'math': 0, "history": 0, "geography": 0}

# for-loop to calculate every subject's marks average and display them
for subject in grades:
    # used to define the variable and later on to reset the value to 0
    subject_total_value: int = 0
    # calculating the sum of mark in a certain subject
    for grade in grades[subject]:
        subject_total_value += int(grade)
    average[subject] = round(subject_total_value / len(grades[subject]))
    # based on the average grade value it displays a motivational sentence
    if average[subject] >= 70:
        print('Your average percentage of marks in ', subject, 'was ', average[subject], ', well done!')
    elif 40 <= average[subject] < 70:
        print('Your average percentage of marks in ', subject, 'was ', average[subject], ', good effort, but keep '
                                                                                         'working')
    elif average[subject] <= 39:
        print('Your average percentage of marks in ', subject, 'was ', average[subject], ', maybe see if you can '
                                                                                         'study with a classmate?')
