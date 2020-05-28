# Substitute
# re.sub(pattern, repl, string, max=0)
# replaces all occurences of RE
mport re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)

#Code removes the hyphen sepereating the digits.
