from datetime import datetime
from datetime import date

curentdate = datetime.now()
print(curentdate)

testdate = date(2023., 3, 1)
print(testdate)

today = date.today()
print("todays date", today)
print(today.month)
print(today.year)
print(today.day)

