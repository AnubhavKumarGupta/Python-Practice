# a = int(input("input the number "))
# for x in range(a, 0, -1):
#     print(x)


def display_calendar(y, m):
    import calendar

    print(calendar.month(y, m))


y = int(input("Enter year: "))
m = int(input("Enter month: "))

display_calendar(y, m)
