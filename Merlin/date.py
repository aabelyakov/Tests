
# Выведи завтрашнюю дату
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

print(tomorrow)

# Выведи "Привет, мир!" на HTML-страницу
print('<html><body>Привет, мир!</body></html>')

# Выведи последнюю дату предыдущего месяца
from datetime import datetime, timedelta

today = datetime.today()

# Дата первого дня текущего месяца
print(today.replace(day=1))

last_month = today.replace(day=1) - timedelta(days=1)
print(last_month.strftime("%Y-%m-%d"))

# Найти последний день текущего месяца
import calendar
import datetime

# Get the current month and year
now = datetime.datetime.now()
year = now.year
month = now.month
print(111, month)

# Get the last day of the current month
_, last_day = calendar.monthrange(year, month)

print("The last day of the current month is {}".format(last_day))

# Найти последний день текущего месяца (второй вариант)
# Первое число следующего месяца
next_month = today.replace(month=month+1,day=1)
print("today", today)
print("next_month", next_month)

# Последний день текущего месяца
cur_month = next_month - timedelta(days=1)
print("cur_month", cur_month)
