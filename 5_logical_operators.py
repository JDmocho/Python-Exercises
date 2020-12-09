# task with logical operator
IsWeekend = True
print('IsWeekend=', IsWeekend)

Temperature = 0
print('Temperature:', Temperature)

Snow = True
print('Snow=', Snow)

GoSkiing = IsWeekend and Temperature <= 0 and Snow
print('GoSkiing', GoSkiing)

# another task
IsWeekend1 = False
print('Is weekend =', IsWeekend)

Temperature1 = 5
print('Temperature =', Temperature)

ToDoList1 = 'Shopping'
print('ToDoList = ', ToDoList1)

IsHappy = not IsWeekend1 and Temperature1 < 20 and ToDoList1 != ''
print('IsHappy=', IsHappy)
