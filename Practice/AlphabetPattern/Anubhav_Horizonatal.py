# Printing the patterns horizontally

patterns = [[], [], [], [], [], [], []]

# First pattern
for row in range(7):
    for col in range(5):
        if (row == 0) and (col in {1, 2, 3}):
            patterns[row].append("*")
        elif (row in {1, 2, 4, 5, 6}) and (col in {0, 4}):
            patterns[row].append("*")
        elif row == 3:
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")  # Add space between patterns

# Second pattern
for row in range(7):
    for col in range(5):
        if (row != 2 and row != 3 and row != 4) and (col == 0 or col == 4):
            patterns[row].append("*")
        elif (row == 2) and (col != 2 and col != 3):
            patterns[row].append("*")
        elif (row == 3) and (col % 2 == 0):
            patterns[row].append("*")
        elif (row == 4) and (col != 1 and col != 2):
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Third pattern
for row in range(7):
    for col in range(5):
        if (row != 6) and (col in {0, 4}):
            patterns[row].append("*")
        elif (row == 6) and (col in {1, 2, 3}):
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Fourth pattern
for row in range(7):
    for col in range(5):
        if (row in {0, 3, 6}) and col in {0, 1, 2, 3}:
            patterns[row].append("*")
        elif (row in {1, 2, 4, 5}) and (col in {0, 4}):
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Fifth pattern
for row in range(7):
    for col in range(5):
        if col == 0 or col == 4:
            patterns[row].append("*")
        elif (row == 3) and (col != 0 and col != 4):
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Sixth pattern
for row in range(7):
    for col in range(5):
        if (row == 0) and (col in {1, 2, 3}):
            patterns[row].append("*")
        elif (row in {1, 2, 4, 5, 6}) and (col in {0, 4}):
            patterns[row].append("*")
        elif row == 3:
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Seventh pattern
for row in range(7):
    for col in range(5):
        if (row not in {5, 6}) and (col in {0, 4}):
            patterns[row].append("*")
        elif (row == 5) and (col in {1, 3}):
            patterns[row].append("*")
        elif (row == 6) and (col == 2):
            patterns[row].append("*")
        else:
            patterns[row].append(" ")
    patterns[row].append("  ")

# Print all patterns
for row in range(7):
    print("".join(patterns[row]))
