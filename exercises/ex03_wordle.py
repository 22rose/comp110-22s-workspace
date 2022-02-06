"""Ex03--structured wordle."""

__author__ = "730480585"


def contains_char(any_length_string: str, single_char: str) -> bool:
    """Searches if the single character is in the string provided. returns true if so, false if not."""
    assert len(single_char) == 1
    does_it_exist: bool = False     
    alt_idx: int = 0
    while not does_it_exist and alt_idx < len(any_length_string):   # while both of these conditions are met we enter the loop
        if any_length_string[alt_idx] == single_char[0]:    # if the current index of string matches the single character
            does_it_exist = True       # does_it_exist variable means true; this means the single character exists somewhere
        else:               
            alt_idx += 1      # if it doesn't we increase index being searched
    if does_it_exist:      # if does it exist is true, it means the character exists, so we return True for the function, if not, return False
        return True                 
    else:
        return False
    

def emojified(guess: str, secret: str) -> str:
    """This will return an emojified version of the guess string, corresponding to whether a character in the guess matches the secret."""
    assert len(guess) == len(secret)  
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    i: int = 0
    while i < len(secret):   # if same character is at the same index of guess and secret, theres a green box
        if guess[i] == secret[i]:
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):  # if contain_char function finds that character in guess does exist (returned True), we print yellow, if not white box
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i = i + 1
    return(result)


def input_guess(expected_len: int) -> str:  
    """Given expected length of a guess, we will prompt user for a guess, and keep doing so till correct length is given."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:  # if the length given does not match length expected, we prompt for another corrent-length guess
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """Establish secret word, keep track of turns, whether user has won, and control flow of game."""
    secret_word: str = "codes"
    turn: int = 1  # we start at 1 cause 1 is the first turn
    won: bool = False
    while turn <= 6 and not won:  # since we have 6 turns, we make it less than or equl to 6
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret_word))  # we collect guess and return that as a string of emojis using emojified function
        emojis = emojified(guess, secret_word)
        print(emojis)
        if guess == secret_word:  # if guess is the same as secret, we print winning comment and how many turns it took
            print(f"you won in {turn}/6 turns!")
            won = True
        turn = turn + 1
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()   