import datetime

longmonth = [1, 3, 5, 7, 8, 10, 12]  # 31天的月份
shortmonth = [4, 6, 9, 11]  # 30天的月份


def calendar(year, month):
    """
    :param year: 年份传参
    :param month: 月份传参
    :return:
    """
    date = datetime.datetime(year, month, 1, 0, 0, 0)  # 将时间设置为传参年月的1号
    result = "Sun\tMon\tTue\tWed\tThu\tFri\tSat\t\n"  # 存储本月每一天的字符串
    # 判断该月为长月还是短月
    if date.month in longmonth:
        days = 31
    elif date.month in shortmonth:
        days = 30
    else:
        # 判断是否是闰年
        if not (date.year % 4) and date.year % 400:
            days = 29
        else:
            days = 28
    num = 0
    # 先获取当前日期为本月第几天，因为打印出的日历表示sun开头，因此加1
    firstweekday = date.weekday() + 1
    # 计算这张日历表的行数
    lenth = (days + firstweekday) // 7 + 1
    # 将日期添加到日历表的指定位置
    for lent in range(1, lenth + 1):
        for lis in range(1, 8):
            num += 1
            if days + firstweekday >= num > firstweekday:
                result += "{}\t".format(num - firstweekday)
            else:
                result += " \t"
        result += "\n"

    return result


# 打印日历
print(calendar(2019, 10))
