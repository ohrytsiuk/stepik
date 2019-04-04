import datetime

y, m, d = map(int, input().split())
n = int(input())

current_date = datetime.date(y, m, d)
add_days = datetime.timedelta(n)
new_date = current_date + add_days
print("{} {} {}".format(new_date.year, new_date.month, new_date.day))
