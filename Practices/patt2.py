# # a=int(input())
# # for i in range (1,a+1):
# #     for j in range (1,i+1):
# #         print('*',end='')
# #     print()

# a=int(input())
# for i in range (1,a+1):
#     print("*"*i)

import pyautogui as pg
import time

# Giving Dealy to run program

print("program will run after 5 second")
time.sleep(5)
print("running")

# Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

# For loop
for i in range(100):
    # writing the messages
    pg.write("Hii Anubhav")
    time.sleep(0.5)
    # Seding the messages by pressing enter
    pg.press("Enter")