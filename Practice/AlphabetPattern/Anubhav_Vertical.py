for row in range(7):
    for col in range(5):
        if (row == 0) and (col in {1, 2, 3}):
            print("*", end=" ")
        elif (row in {1, 2, 4, 5, 6}) and (col in {0, 4}):
            print("*", end=" ")
        elif row == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()


for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if (row != 2 and row != 3 and row != 4) and (col == 0 or col == 4):
            print("*", end=" ")
        elif (row == 2) and (col != 2 and col != 3):
            print("*", end=" ")
        elif (row == 3) and (col % 2 == 0):
            print("*", end=" ")
        elif (row == 4) and (col != 1 and col != 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()

for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if (row != 6) and (col in {0, 4}):
            print("*", end=" ")
        elif (row == 6) and (col in {1, 2, 3}):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()


for row in range(7):
    for col in range(5):
        if (row in {0, 3, 6}) and col in {0, 1, 2, 3}:
            print("*", end=" ")
        elif (row in {1, 2, 4, 5}) and (col in {0, 4}):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

print()

for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if col == 0 or col == 4:
            print("*", end=" ")
        elif (row == 3) and (col != 0 and col != 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()


for row in range(7):
    for col in range(5):
        if (row == 0) and (col in {1, 2, 3}):
            print("*", end=" ")
        elif (row in {1, 2, 4, 5, 6}) and (col in {0, 4}):
            print("*", end=" ")
        elif row == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()


for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if (row not in {5, 6}) and (col in {0, 4}):
            print("*", end=" ")
        elif (row == 5) and (col in {1, 3}):
            print("*", end=" ")
        elif (row == 6) and (col == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


