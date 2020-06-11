import csv

%precision 2

# Opening a file
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.

# Column names in the CSV file
print(mpg[0].keys())

# to find the city fuel economy
print(sum(float(d['cty']) for d in mpg) / len(mpg))

# to find the highway fuel economy
print(sum(float(d['hwy']) for d in mpg) / len(mpg))

# to find the unqiue values number of cylinders in our list
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)


# Grouping cars by number of cylinder and finding avg city mpg
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl


# To find the unique class types in our dataset
vehicleclass = set(d['class'] for d in mpg) # what are the class types
vehicleclass

# To find average highway mpg in our dataset
HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass

