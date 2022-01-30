"""example of looping through all characters in a string"""

user_string: str = input("Give me a string! ")
# we ask the user for a string, they give us a string input, 
# and now we want to loop through all the 
# characters in the string and print them one by one by one

# The varibale "i" is a common counter variable name in programming
# i is short for iteration
i: int = 0        # we start with 0 because index starts at 0
while i < len(user_string):
    print(user_string[i])       # the string the user inputted, go to index i which is initially zero(first character),
                                # print that character
                                # then add 1 to the index, and if that number is less than the length (amount of characters)
                                #  in the given string, print 
                                 # the first index(second character) and so on and so forth as long as condition is met
    i = i + 1
print("Done!")
