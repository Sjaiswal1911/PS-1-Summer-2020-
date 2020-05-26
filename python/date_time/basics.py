# Date and Time basics

# Time Tuple
# Many of the Python's time functions handle time as a tuple of 9 numbers, as shown below −
# Index   Field           Values
# 0	  4-digit year	      2016
# 1	  Month	              1 to 12
# 2	  Day	                1 to 31
# 3	  Hour	              0 to 23
# 4	  Minute            	0 to 59
# 5	  Second	            0 to 61 (60 or 61 are leap-seconds)
# 6	  Day of Week	        0 to 6 (0 is Monday)
# 7	  Day of year	        1 to 366 (Julian day)
# 8	  Daylight savings	 -1, 0, 1, -1 means library determines DST
# For Example −


# Current Time
# time.localtime()
# returns the current time in form of time tuple
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)


# Formatted time
# returns time in format:
# Day Month Date Time(HH:MM:seconds) year
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time in formatted way :", localtime)


# Getting calendar
# calendar.(year,month)
# returns a calendar for the specififed month
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

 #
