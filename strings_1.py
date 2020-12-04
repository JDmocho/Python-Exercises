text = 'Always look on the bright side of life.'

#Display text in capital letters.
print(text.upper())

#Display text in lower letters.
print(text.lower())

#Check the sentence ends with the word "life."
print(text.endswith('life.'))

#Check the sentence is in capital letters
print(text.isupper())

#Check the sentence converted to uppercase is in uppercase
print(text.upper().isupper())

#Find the position of the word "of" in the sentence
print(text.find('of'))

#Replace the word "bright" with "dark"
print(text.replace('bright','dark'))

#Replace the word "bright" with "dark" and "life" with "power"
print(text.replace('bright','dark').replace('life','power'))

#Separate the sentence according to the separator of the space
print(text.split(' '))

#Check the sentence is: a number, a decimal number, a string without numbers, a string with letters and numbers
print(text.isdigit())
print(text.isdecimal())
print(text.isalpha())
print(text.isalnum())