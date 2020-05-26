# Calenndar Module

# First Weekday
# Calendar.firstweekday()
# Returns the current setting for the weekday that starts each week.
# default is Monday i.e '0'
import calendar
print(calendar.firstweekday())


# Leap year
# calendar.isleap(year)
# returns true if the year is ;eap year, else false
year = 2020
print("Is 2020 a leap year?" , calendar.isleap(2020))


# Leap days
# calendar leapdays(y1. y2)
# Returns the total number of leap days within range [y1,y2]
y1 = 2020
y2 = 2021
print("No. of leap days this year:" , calendar.leapdays(y1,y2))


# Calendar of month
# calendar.month(year,month,w,l)
# Retruns multiline stirng of the calendar for Month
# w is width of chars of each date, l is lines for each week
year = 2020
month = 5
calendar.month(year,month,w=2, l =1)
