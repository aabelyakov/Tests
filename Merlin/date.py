import calendar
import datetime
from datetime import date


# Выведи завтрашнюю дату
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)


# Выведи последнюю дату предыдущего месяца
today = datetime.datetime.today()

# Дата первого дня текущего месяца
print(today.replace(day=1))

last_month = today.replace(day=1) - datetime.timedelta(days=1)
print(last_month.strftime("%Y-%m-%d"))

# Найти последний день текущего месяца
# Get the current month and year
now = datetime.datetime.now()
year = now.year
month = now.month
print(111, month)

# Get the last day of the current month
_, last_day = calendar.monthrange(year, month)

print(f"Последний день текущего месяца - {last_day}")

# Найти последний день текущего месяца (второй вариант)
# Первое число следующего месяца
next_month = today.replace(month=month + 1, day=1)
print("today", today)
print("next_month", next_month)

# Последний день текущего месяца
cur_month = next_month - datetime.timedelta(days=1)
print("cur_month", cur_month)

# Here are some examples of how to use the datetime module in Python:

# To get the current date and time:
now = datetime.datetime.now()
print("now", now)

# To format the date and time:
now = datetime.datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print("formatted_date", formatted_date)

# To create a datetime object from a string:
date_string = '2020-02-10'
date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
print("date_object", date_object)

# To add or subtract time from a datetime object:
now = datetime.datetime.now()

# add one day
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print("tomorrow", tomorrow)

# subtract one hour
one_hour = datetime.timedelta(hours=1)
one_hour_ago = now - one_hour
print("one_hour_ago", one_hour_ago)


current_date = date.today()
print(current_date)

print(datetime.datetime.today())
print(datetime.datetime.now())

# datetime Python ...
# https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python
#
# datetime Python.
# https://docs-python.ru/standart-library/modul-datetime-python/primery-ispolzovanija-datetime-datetime/
