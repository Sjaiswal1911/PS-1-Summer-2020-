 Regular Expressions
# Special sequence that helps you match or find strings
# the module 're' provides full support for perl like Regular Expressions

# Match Object Method
# re.match(pattern, string, flags = 0)
# pattern : This is the regular expression to be matched
# string : String to be searched for matches
# flags  :specify different flags
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
