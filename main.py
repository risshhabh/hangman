from random import choice  # Randomly pick a word.

filename = r"secret.txt"

# Remove all comments from `secret.txt`
try:
    with open(filename, "r+") as f:
        file = [line.strip() for line in f.read().splitlines()]

        # Remove all comments from list of lines in `filename`.
        for ind, val in enumerate(file):
            if len(val) == 0 or val[0] == "#":
                file.pop(ind)
except FileNotFoundError:
    print("Hmm... it seems like your file does not exist. I made it for you, please enter some words into it.")
    open(filename, "x")
    exit()

# Choose word, if file is empty, end program.
try:
    word = choice(file)
except IndexError:
    print(
        f"""\
You haven't chosen a word.
Please input the words into `{filename}` and rerun the program."""
    )
    exit()

length = len(word)
guess = list("_" * length)  # Replace "_" with correct characters with every guess.

print("Let's play hangman! Try guessing the word:")

correct = False
guesses = 6

while guesses > 0:
    if correct == True:
        break

    print(*guess, sep=" ")
    char = input("Enter a character, or the entire word if you know it. \n--> ")

    if char == word:
        guesses -= 1
        correct = True

    elif len(char) == length:
        print("That is not the word! Try again.")
        guesses -= 1

    elif len(char) != 1:
        print(
            "You have entered something more than one character; that is not allowed. Try again."
        )
        # Don't subtract from guesses for invalid input.

    elif char in word:
        for ind, val in enumerate(word):
            if char == val:
                guess[ind] = char

                if "".join(guess) == word:
                    correct = True
        guesses -= 1

    else:  # if `char` not in word and is one character long.
        guesses -= 1


if correct:
    print(f"You guessed the word {word} in {6 - guesses} tries!")

else:
    print(f'The word was "{word}", you weren\'t able to guess it. Maybe next time?')
