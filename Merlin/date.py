
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