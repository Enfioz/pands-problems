# Patrick Corcoran
# A program that outputs whether or not 
# today is a weekday or is the weekend.

import datetime

now = datetime.datetime.now()
current_day = now.weekday
weekend = (5,7)

if current_day == weekend:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")

time_diff = datetime.timedelta(days = 4)
future_day = now + time_diff
weekend = (5,7)

if future_day == weekend:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
