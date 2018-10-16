states = {
    'oregon': 'or',
    'florida': 'fl',
    'californica': 'ca',
    'new pork': 'ny',
    'michichigans': 'mi'
}

cities = {
    'ca': 'san francisca',
    'mi': 'detroit',
    'fl': 'jacksonvillage'
}

cities['ny'] = 'new pork'
cities['or'] = 'portlando'

print '-' * 10
print 'ny state has '+ cities['ny']
print 'OR state has '+ cities['or']

print 'new pork short is ' + states['new pork']

print 'michigan is '+ cities[states['michichigans']]
print 'flordozy has'+ cities[states['florida']]

print '-' * 10

for state, abbrev in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)

print '-' * 10

for state, abbrev in states.items():
    print "%s state is abbreviated as %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
