# Write down your shoe number and multiply by 5. Add 50 to that.
# Multiply this by 20, then add 1017. Subtract your birth year from that.
# A 4 digit number has come out. The first two digits are your shoe number and the last two are your age.

print((38*5+50)*20+1020-1986)

# Think a non-negative integer. Multiply it by 2, add 10, divide by 2, subtract the starting number.
# There should be 5 - always.

print((7*2+10)/2-7)

# The lecturer tells the students. You will pass a semester if you have at least 80% attendance and average> = 3.0,
# or if you have successfully completed a term paper. Build a Python expression that will tell
# if a student who has an 0.85 presence, a 3.5 average and a failed termination test.

presence = 0.85
average = 3.5
job = False

passed = presence > 80 and average >= 3.0 or job == True
print('Did you pass:', passed)

# The lecturer changed his mind. In order to pass a semester you must: have at least 80% attendance,
# a sequence> = 3.0 and a completed work. Will the student pass now?

passed = presence > 80 and average >= 3.0 and job == True
print('Did you pass: ', passed)

# We are changing the student's data. Now it has a presence of 40%.
# Average 2.5, but completed a term paper. Check according to which criteria the student will complete the semester.

presence1 = 40
average1 = 2.5
job1 = True

passed1 = presence1 > 80 and average1 >= 3.0 or job1 == True
print('Did you pass: ', passed1)

