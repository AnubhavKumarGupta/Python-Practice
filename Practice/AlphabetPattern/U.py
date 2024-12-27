for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if (row != 6) and (col in {0, 4}):
            print("*", end=" ")
        elif (row == 6) and (col in {1, 2, 3}):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
