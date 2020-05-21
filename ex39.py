#creates a mapping of state to abbreviation
states = {
        'Maharashtra' : 'MH',
        'Delhi' : 'DL',
        'Punjab' : 'PB',
        'Goa' : 'GA',
        'Karnataka' : 'KA'
}

#create a basic set od states and some cities in them
cities = {
        'MH' : 'Mumbai',
        'KA' : 'Bangalore',
        'DL' : 'Delhi'
}

#add some more cities
cities['GA'] = 'Goa'
cities['PB'] = 'Chandigarh'

#print out some cities

print('-' * 15)
print("MH state has: ", cities['MH'])
print("GA state has: ", cities['GA'])

#print some states
print('-' * 15)
print("Punjab's abbreviation is:" , states['Punjab'])
print("Karnataka's abbreviation is:", states['Karnataka'])

#do it by using state then cities dict
print('-' * 15)
for state,abbrev in list(states.items()):
    print(f"{state} has the city {cities[abbrev]} ")
