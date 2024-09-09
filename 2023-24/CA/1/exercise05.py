# task:
#
# Exercise 5)
# Write a program to discuss the Avengers by employing the match statement. Your program should:
# • Take in the name of an Avenger the user really likes.
# • Check it against 5 different Avengers (using a match statement). You can choose which Avengers to
# accept. At least one Avenger should be checked using a combined case of its full name and at least one
# nickname.
# o If the name entered matches any of the Avengers you have specified, you should print a message
# talking about how cool that avenger is.
# o If the name entered DOESN’T match any of your specified Avengers, you should print a message
# saying “I’ll have to look into X, I can’t believe I haven’t heard of them!”

# using the match-case statement the program could decide which answer to display according to user's input

match input('please enter an Avenger you would like to discuss about '):
    case 'Tony Stark' | 'Iron Man':
        print('I like him too, he is a genius with high tech suits. Lately he has AR glasses. Pretty cool')
    case 'Steve Rogers' | 'Captain America':
        print('Captain America is cool for his courage and superhuman strength.')
    case 'Natasha Romanoff' | 'Black Widow':
        print('Natasha is the most confident woman here with extreme combat skills.')
    case 'Wanda Maximoff' | 'Scarlet Witch':
        print('Nice she is the most powerful witch. She could destroy worlds because she read the Darkhold.')
    case 'Clint Barton' | 'Hawkeye':
        print('Clint is the post accurate archer. Lately he was using some high tech arrows to enhance his abilities.')
    case default:
        print("Oh shit I rly don't know who you are talking about I'll have to make a research on it.")
