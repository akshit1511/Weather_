import datetime
n = int(input('days '))

datentime = datetime.datetime.today() + datetime.timedelta(days = n)
print(datentime)