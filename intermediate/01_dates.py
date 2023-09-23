from datetime import datetime

now = datetime.now()

print(f"{now.year}-{now.month}-{now.day}")

first_of_year = datetime(2023, 1, 1)


def print_date(date):
    print(f"{date.year}-{date.month}-{date.day}")


print_date(first_of_year)

from datetime import time, date, timedelta

current_time = time(16, 25, 53)

print(current_time)

makeup_date = date(2017, 6, 6)

print(makeup_date)

current_date = date.today()

print(current_date)

added_date = date(makeup_date.year, makeup_date.month + 1, makeup_date.day)

print(added_date)

time_delta = timedelta(5)

substraced_date = added_date - time_delta

print(substraced_date)
