for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if (row == 0 or row == 3) and (col != 4):
            print("*", end=" ")
        elif (row == 1 or row == 2) and (col == 0 or col == 4):
            print("*", end=" ")
        elif (row == 4) and (col == 0 or col == 2):
            print("*", end=" ")
        elif (row == 5) and (col == 0 or col == 3):
            print("*", end=" ")
        elif (row == 6) and (col == 0 or col == 4):
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
