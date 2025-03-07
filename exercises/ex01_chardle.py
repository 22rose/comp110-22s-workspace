"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480585"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_character_word)

counting_variable_for_instances: int = 0 

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
    counting_variable_for_instances = counting_variable_for_instances + 1 
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
    counting_variable_for_instances = counting_variable_for_instances + 1
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    counting_variable_for_instances = counting_variable_for_instances + 1
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
    counting_variable_for_instances = counting_variable_for_instances + 1
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
    counting_variable_for_instances = counting_variable_for_instances + 1
if counting_variable_for_instances > 1:
    print(str(counting_variable_for_instances) + " instances of " + single_character + " found in " + five_character_word)
else:
    if counting_variable_for_instances == 1:
        print(str(counting_variable_for_instances) + " instance of " + single_character + " found in " + five_character_word)
    else:
        if counting_variable_for_instances == 0:
            print("No instances of " + single_character + ' found in ' + five_character_word)
    
                