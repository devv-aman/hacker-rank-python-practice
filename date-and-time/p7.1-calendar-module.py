# Problem: https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
date_str = list(map(int, input().split()))
print(["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"][calendar.weekday(date_str[2], date_str[0], date_str[1])])
