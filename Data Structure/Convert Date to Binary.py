def convertDateToBinary(date):
    parts = date.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    return f"{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}"



date = "1900-01-01"
print(convertDateToBinary(date))