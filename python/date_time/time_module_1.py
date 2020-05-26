# Time Module
# functions for working with times .

# Alternate Zone
# time.altzone()
# This method returns the offset of the local DST timezone, in seconds west of UTC, if one is defined.
import time
print ("time.altzone : ", time.altzone)


# ascTime
# time.asctime(tupletime)
# Accepts a time tuple and returns a 24 char long string
# Format : Day Month Date Time year
t = time.localtime()
print ("asctime : ",time.asctime(t))


# Clock
# time.clock()
# Returns the current CPU in floatingpoint no. of seconds
# useful to measure compputational costs of approaches
def procedure():
   time.sleep(2.5)

# measure process time
#t0 = time.clock()
#procedure()
#print (time.clock() - t0, "seconds process time")

# measure wall time i.e real world time elapsed
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")

