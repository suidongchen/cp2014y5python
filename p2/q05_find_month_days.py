month = input("Please enter the month (Jan=1, Dec=12): ")
year = input("Please enter the year: ")

dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if year % 400 == 0:
    leap = 1
elif year % 100 == 0:
    leap = 0
elif year % 4 == 0:
    leap = 1
else:
    leap = 0

days = dic[month] + leap
print days
