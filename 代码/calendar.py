import datetime

longmonth = [1, 3, 5, 7, 8, 10, 12]
shortmonth = [4, 6, 9, 11]


def calendar(year, month):
    date = datetime.datetime(year, month, 1, 0, 0, 0)
    result = "Sun\tMon\tTue\tWed\tThu\tFri\tSat\t\n"
    if date.month in longmonth:
        days = 31
    elif date.month in shortmonth:
        days = 30
    else:
        if not (date.year % 4) and date.year % 400:
            days = 29
        else:
            days = 28
    num = 0
    firstweekday = date.weekday() + 1
    lenth = (days + firstweekday) // 7 + 1
    for lent in range(1, lenth + 1):
        for lis in range(1, 8):
            num += 1
            if days + firstweekday >= num > firstweekday:
                result += "{}\t".format(num - firstweekday)
            else:
                result += " \t"
        result += "\n"

    return result



print(calendar(2016,2))