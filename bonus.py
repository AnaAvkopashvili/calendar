def months(month, year):
    days_in_month = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days_in_month = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days_in_month = 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month = 29
        else:
            days_in_month = 28
    return days_in_month


def calendar(date):
    output = ""
    x = date.split("-")
    month = int(x[0])
    year = int(x[1])
    dic1 = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
           8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    output += ((dic1[month] + " " + str(year)).center(26, ' '))
    output += "\n"
    week = "Su  Mo  Tu  We  Th  Fr  Sa"
    output += week
    output += "\n"

    if month == 1:
        month = 13
        year -= 1
    if month == 2:
        month = 14
        year -= 1
    first_day = int((1 + 13 * (month + 1) // 5 + year % 100 + (year % 100) // 4 +
                         (year // 100) // 4 - 2 * (year / 100)) % 7)
    year += 1
    if month == 14:
        month = 2
    if month == 13:
        month = 1
    output += "    " * first_day

    if first_day == 0:  # sunday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d} " + "\t"
            if i % 7 == 0:
                output += "\n"
    if first_day == 1:  # monday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d}" + "\t"
            if i == 6 or i == 13 or i == 20 or i == 27:
                output += "\n"
    if first_day == 2:  # tuesday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d}" + "\t"
            if i == 5 or i == 12 or i == 19 or i == 26:
                output += "\n"
    if first_day == 3:  # wednesday
        for i in range(1, months(month, year) + 1):
            print(f"{i:2d}" + "\t", end="")
            if i == 4 or i == 11 or i == 18 or i == 25:
                output += "\n"
    if first_day == 4:  # thursday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d}" + "\t"
            if i == 3 or i == 10 or i == 17 or i == 24 or i == 31:
                output += "\n"
    if first_day == 5:  # friday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d}" + "\t"
            if i == 2 or i == 9 or i == 16 or i == 23 or i == 30:
                output += "\n"
    if first_day == 6:  # saturday
        for i in range(1, months(month, year) + 1):
            output += f"{i:2d}" + "\t"
            if i == 1 or i == 8 or i == 15 or i == 22 or i == 29:
                output += "\n"
    return output


if __name__ == '__main__':
    data = input("Enter: ")
    print(calendar(data))