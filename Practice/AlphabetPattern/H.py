for row in range(7):  # 0 to 6
    for col in range(5):  # 0 to 4
        if col == 0 or col == 4:
            print("*", end=" ")
        elif (row == 3) and (col != 0 and col != 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
