 Ctime
# time.ctime(secs)
# Like asctime(localtime(secs)) and without arguments is like asctime( )
print ("ctime : ", time.ctime())


# sleep
# time.sleep(secs)
# Suspends the calling thread for 'secs' seconds
print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())


# time
# time.time()
# Returns the current time instant, a floating-point number of seconds since the epoch.
print ("time.time(): %f " %  time.time())
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))


#String format time
# time.strptime(str.fmt = "")
# Parses str according to string format
struct_time = time.strptime("30 12 2015", "%d %m %Y")
print ("tuple : ", struct_time)


# Time set
# time.tzset()
# Resets time conversion rules

# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# time.tzset()
#print (time.strftime('%X %x %Z'))
