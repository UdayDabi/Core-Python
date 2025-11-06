import datetime

today = datetime.date.today()

future = today + datetime.timedelta(days=5)
past = today - datetime.timedelta(days=5)
print("Today's date is:", today)
print("Date after 5 days will be:", future)
print("Date before 5 days was:", past)
