Task:

Exercise 1)
Write a function that validates an email address. Your function should take in a single parameter – the string to be
validated as an email address – and should return True if the string is a legitimate email address and False
otherwise. A string is considered an email address if:
• It contains exactly one @. There must be at least one character before the @.
• It contains at least one '.' AFTER the @. There must be a text before and after the '.' .

Analysis:
    The goal is to check few parameters of the string. I decided to use splits instead of looping the whole string.
    The conditions for function to return false:
        -   there are not any at signs
        -   there are more than one at signs
        -   no value before at sing or after
        -   the end has to hasn't got 2 characters
        -   there is not any dot after at sign
    The function would just split the string into areas where any of these errors can happen so is's easier to find them.
    The regex pattern would be: "^\w+@\w+\.\w{2}$"
Pseudocode:
    verify_email(email)
        email split by @
        check if it has two parts
            (if it does, it continues and email last part split by and check if it has two at least parts and check the
            \last one if it has 2 characters and check if the first part starts with a character and check if there is
            \a character in the first part of the mail)
            returns True
            else it returns False
Sandbox-mode:
    import regex library
    create function verify_email(mail)
    set pattern as "^\w+@\w+\.\w{2}$"
    check if the mail suits that pattern return True xor False

Exercise 2)
Write a program that allows a user to write an email. Your program should prompt the user to enter the following:
• Subject
• Recipient (an email address. Your program should validate this using your function from exercise 1 and
should not proceed until a valid email has been entered)
• Message body
Once this information has been read in, your program should append them to the file for the specified recipient
(i.e. a file with the name matching the recipient’s email address). You should use an appropriate delimiter to
separate the information making up the email when writing it to the file.

Analysis:
    - input: email subject, recipient, text
    - output: created file with name reciepient email, and inside is subject and email body
Pseudocode:
    asks about sender email
    passes it into the whole function get_email_to_send
    gets file and stores it into variable file based on the recipient email
    and just calls function send_email with argument email and file where it is going to be stored

    function get_email_to send
        While loop until sender email is valid from input
        While loop that ends only if the recipient email address is correct based on the correct_email bool variable
            check via function from exercise1 is it is correct
            if it is
                set correct_email bool variable to true
            else
                prompt for another email
        Ask for a subject and store it into variable
        Ask for the text and store it into variable
        return all 4 attributes as tuple

    function to send / store mail called send_mail with argumtents of mail attributes as tuple and file where it will be
            stored
        for loop looping content type and mail attributes and creating a line to be written in file, provisionally
            stroed in a list
        at the end it adds one line with datetime when is it created
        writes all lines and cloes the file

    Function to get a file based on recipient mail address
        it checks if such file exists
            if yes it returns the file with mode: 'a'
        else
            it returns a file with mode 'w' so the file would be created and empty


Exercise 3)
Write a program that asks the user to enter their email address, then reads in the contents of their email file, i.e.
the file with a name matching their email address (generated in the previous exercise) into a list of tuples (each
email should be stored as a tuple). Your program should repeatedly offer the following menu:
• Sort the emails:
o By sender (ascending)
o By date received (descending)
o By subject (ascending)
• Display all emails
• Exit
Hint: You will need to make sure the structure this program uses to parse the emails out of the file matches the
structure used in the previous application.

    Analysis:
        Part one:
            -   input: correct email
            -   output: ask for one of the following
        Part two:
            -   input: sort by sender / sort by date / sort by subject / display all emails / exit
            -   output: output is based on the input and reads all the data from file
        Data storage:
            data taken loaded from file is about to be stored as a list of tuples, each tuple is a mail
            [(sender, subject, datetime, text), (sender, subject, datetime, text)...]
    Pseudocode:
        takes in recipient email and passes it to email verification function that checks if such email address is
            correct, if not asks for another one
        file path would be retireved via function get file path to read with argument of recipient email
            the file path is tuple, (bool, string) if such file exists and the path
        if file path bool is true
            reads in mails from file based on the file path using read_emails function and store it into mails variable
            calls interact with mails function passing mails variable
        else
            the file does not exists so it prints the passed report from file path tuple which means there are no
                incoming mails, nothing to interact with

        function email_verification passing recipient email
            while loop until input email is verified to true from function verify_email
                returns recipient email

        function to get file path passing recipient email
            if file exists
                returns True and path to the file
            else returns False and report string

        function read_emails passing file_path with valid path to the file
            opens file with mode 'r'
            starts reading each line stripped and split with ### until it reaches date time
                which is the last mail attribute and appends it into mail list
                when it reaches the last attribute it just clears the mail list and  content is appended into mails list
            when all lines are read it closes the file and returns mails as list of mails incoming to recipient email
                address with pre-defined attributes

        function display all mails passing mails variable
            for loop to print each attribute of mail

        function sort mails sender passing mails variable
            sorts mails using function sorted where the sorting variable is mails and the key is the sender email
                address such function is used to define multidimensional list indexing to sort
            returns sorted mail

        function sort mails by subject
            same as before but different key, which is the subject value from it's tuple
            returns sorted mails

        function sort mails by date
            same as before but different key, which is the date value from it's tuple
            returns sorted mails

        function interact with mails
            while loop until quit not initiated
                user input is taken, should have been int
                check if it is digit
                    if so check if it is in requested range
                        if so use match statement to call resolved function and display them afterwards
                    else print report that it is number out of range
                else print to insert a number
