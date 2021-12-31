from random import choice  # Randomly pick a word.

filename = r"secret.txt"

# Remove all comments from `secret.txt`
with open(filename, "r+") as f:
    file = [line.strip() for line in f.read().splitlines()]

    # Remove all comments from list of lines in `filename`.
    for ind, val in enumerate(file):
        if val[0] == "#":
            file.pop(ind)


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
