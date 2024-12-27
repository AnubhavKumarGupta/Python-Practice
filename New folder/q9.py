# NUMBER GUESSING GAME
winning_number = 45
user = int(input("Input the number:"))
if (winning_number == user):
    print("YOU WON!!!!")
elif (user > winning_number):
    print("too high")
else:
    print("too low")
