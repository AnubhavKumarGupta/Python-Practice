h = int(input())
if (4 <= h <= 6):
    print("Breakfast")
elif (12 <= h <= 13):
    print("Lunch")
elif (16 <= h <= 17):
    print("Snacks")
elif (19 <= h <= 20):
    print("Dinner")
elif (h <= 0 and h> 24):
    print("Wrong Time")
else:
    print("Patience is a virtue")
