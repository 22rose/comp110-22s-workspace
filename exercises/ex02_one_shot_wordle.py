"""EX02 - one shot wordle."""

__author__ = "730480585"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")  # we initially ask user for input

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")  # if the user doesn't have 6 characters, we prompt them for another

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
result: str = ""
while i < len(secret):     # while the index int is less than the length of our secret
    if guess[i] == secret[i]:    # if the character of guess matches the character of secret at the same index, append green
        result += GREEN_BOX    
    else:                      # else we are going to check the index of the guess against indexes of secret to find a match
        does_it_exist: bool = False     
        alt_idx: int = 0
        while not does_it_exist and alt_idx < len(secret):    # while both of these conditions = True
            if secret[alt_idx] == guess[i]:  # if alt_idx of secret==to index of guess, it is True and we code to append yellow below
                does_it_exist = True    # this means the character exists, just at different indexes. if not, we code to append white below
            else:               
                alt_idx += 1   # this is where we increase alt. index of secret to loop back and check against the index of guess
        if does_it_exist:              
            result += YELLOW_BOX      
        else:
            result += WHITE_BOX
    i = i + 1
print(result)

winning_msg: str = "Woo! You got it!"
try_again_msg: str = "Not quite. Play again soon!"
if guess != secret:     # we print a game over comment if the input is the appropriate length but not the secret
    print(f"{try_again_msg}")
else:
    print(f"{winning_msg}")  # we print a winning comment if they input the secret