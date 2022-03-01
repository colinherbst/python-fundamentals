print("Hello World")

# Can you make a typo that generates an error?
# Yes, the error I received is in the next comment.
# NameError: name 'prit' is not defined. Did you mean: 'print'?

# Can you make sense of the error message?
# Yes, the error message is telling me what is misspelled and gives me a suggestion on what I meant.

# Can you make a typo that doesn't generate an error?
# Yes, I misspelled the word Hello.

# Why do you think it didn't make an error?
# This didn't make an error because it is just printing what is typed in the quotes.

# The Zen Of Python output shows 19 ideas to follow when writing code to make it simple and readable.

# On my separate program I assigned a message to a variable and then used that variable in my print statement
# I then changed the value of the variable and re printed the message


def display_message():

    """Display a message about what you are learning in this chapter"""
    print("In this chapter I am learning how to write functions that print text")


display_message()

# I assigned a function to print a message


def favorite_book(title):

    """Display a message saying my favorite book"""
    title = "Alice in Wonderland"
    print(f"My favorite book is {title.title()}!")


favorite_book("title")

# I assigned the function to print the title of my favorite book by assigning the name of that book to "title" and then
# I printed the statement.






