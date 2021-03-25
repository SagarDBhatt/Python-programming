import calendar

month, date, year = map(int, input().split())
strDay = calendar.weekday(year, month, date)
# print(strDay)
print(calendar.day_name[strDay].upper())
