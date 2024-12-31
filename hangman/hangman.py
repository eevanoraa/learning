import random
import json
import os

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, 'words.json'))
    list = json.load(f)
    word = random.choice(list)

    
    guesses = ''
    turns = 12

    while turns > 0:
        failed = 0
        for char in word:

            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break

        print()
        guess_test = ""

        while len(guess_test) != 1 or guess_test in guesses or guess_test.isdigit():
            guess_test = input("Guess a character: ")
            if len(guess_test) != 1 or guess_test in guesses or guess_test.isdigit():
                print("Only one character and don't repeat guesses")
                continue
        else:
            guess = guess_test

        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, 'more guesses')
            if turns == 0:
                print("You Lost")
                print("The word was", word)

        print("\n")
    

if __name__ == "__main__":
    main()