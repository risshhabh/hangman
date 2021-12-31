filename = r"secret.txt"

# Remove all comments from `secret.txt`
with open(filename, "r+") as f:
    file = [line.strip() for line in f.read().splitlines()]  # Strip whitespaces.

    # Remove all comments from list of lines in `filename`.
    for ind, val in enumerate(file):
        if val[0] == "#":
            file.pop(ind)
