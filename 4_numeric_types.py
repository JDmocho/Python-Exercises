# Print the message variable using the% operator

name = 'Joanna'
age = 18
favorite = 7

message = '%s is %d and her favorite number is %d'

print(message % name, age, favorite)

# Other solution

message = '{0:s} is {0:d} and her favorite number is {0:d}'

print(message)

# Finding the result of integer division and the remainder of the division

a = 1234567890
b = 12345

i = a // b
d = a % b

print('1234567890 divided by 12345 is ' + str(i) + ' and the rest is ' + str(d))
