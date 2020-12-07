# % operator

hello = 'Hello %s'
print(hello % ('Bruce'))
print(hello % ('Sue'))

# Format method
hello = 'Hello {0:1}'
print(hello.format('Bruce'))
print(hello.format('Sue'))

# Displaying messages using the % operator

hello1 = '%s has %d %s'
print(hello1 % ('Sue', 1, 'animal.'))
print(hello1 % ('Bruce', 1000000, '$.'))

# Displaying messages using the format method

helloMessage7 = '{0:s} has {1:d} {2:s}'
print(helloMessage7.format('Kate', 1, 'animal'))
print(helloMessage7.format('Chris', 100000, '$'))

# % operator

line = '%s20 costs %d20 €'

print(line % ('ICE CREAM', 3))
print(line % ('TRIP TO VENICE', 119))
print(line % ('PIZZA HAWAI', 6))
