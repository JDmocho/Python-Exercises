# extracting individual elements in the string

message = 'Document "CV.doc" was printed on printer: XEROX'

print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':') + 2:])

print(message[message.find('"') + 1:])

tmp = message[message.find('"') + 1:]
print(tmp[:tmp.find('"')])

print('------------------------------------------')

# write the text "THE EYES" to the variable q. Display the string composed of the letters of the variable q in the order: 0,1,2,5,3,7,4,6.

q = "THE EYES"

print(q)
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

print('------------------------------------------')

# write "a gentleman" to the variable q and then display the letters in the order 3,6,7,2,0,4,5,1,8 - to the end

q1 = "a gentleman"

print(q1)
print(q1[3], q1[6], q1[7], q1[2], q1[0], q1[4], q1[5], q1[1], q1[8:])
print(q1[3] + q1[6] + q1[7] + q1[2] + q1[0] + q1[4] + q1[5] + q1[1] + q1[8:])

print('------------------------------------------')

# make "HERE COME DOTS" out of the words "THE MORSE CODE"? Use the "from-to" notation wherever possible

q = "THE MORSE CODE"

# HERE COME DOTS

print(q[1:3], q[6], q[8], q[3], q[10:12], q[4], q[13], q[9], q[12], q[5], q[0], q[7])

print('------------------------------------------')

# You need to extract the program title and the time it will be broadcast. For this purpose:
# 1. In the variable line enter the text "'Program "Dot nad i" we will send at: 22:00'"
# 2. Extract only the hour into the variable time (you need to look for a colon and get all further characters)
# 3. Display time
# 4. For the tmp variable, extract the text fragment from the line variable that begins after the quotation mark to the end
# 5. For the title variable, extract the text fragment from tmp from the beginning to the quotation mark
# 6. Display title and time

line = 'Program "Kropka nad i" nadamy o: 22:00'

time = line[line.find(':')+2 :]
print(time)

tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)

print('------------------------------------------')

program = 'Program "Pytanie na śniadanie" nadamy o: 6:00'

time1 = program[program.find(':')+2:]
print(time1)

tmp1 = program[program.find('"'):]
print(tmp1)

title1 = tmp1[:tmp1.find('"')]
print(title1)