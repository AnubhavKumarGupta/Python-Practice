import calendar


def main():
    cal = calendar.TextCalendar()
    monthcal = cal.formatmonth(2024, 1)
    print(monthcal)
    with open("monthcal.txt", "w") as f:
        f.write(monthcal)
    f.close()
    yearcal = cal.formatyear(2024)
    print(yearcal)
    with open("yearcal.txt", "w") as f:
        f.write(yearcal)
        f.close()


main()
