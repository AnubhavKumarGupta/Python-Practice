# # NUMBER GUESSING GAME
# winning_number = 45
# user = int(input("Input the number:"))
# if (winning_number == user):
#     print("YOU WON!!!!")
# elif (user > winning_number):
#     print("too high")
# else:
#     print("too low")


w = 45  # winning Number
g = 1  # guessing a number, it will tell user that how many time you run the loop
u = int(input("Input the number:"))
game_over = False

while not game_over:

    if (w == u):

        print(f"YOU WON!! and you guessed this number in {g} times")
        game_over = True
    elif (u > w):
        print("too high")
        g += 1
        u = int(input("Guess again: "))
    else:
        print("too low")
        g += 1
        u = int(input("Guess again: "))
