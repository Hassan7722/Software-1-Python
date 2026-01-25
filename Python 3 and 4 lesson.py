#WHILEEEEEEEEEEEEEE
from idlelib.debugobj_r import remote_object_tree_item

rounds = int(input("Enter number of rounds: "))

finished_rounds = 0
while finished_rounds < rounds:
    print('Oui Oui')
    finished_rounds = finished_rounds + 1

Correct_Password = 'Python123'
password = input('Enter password: ')
while password != Correct_Password:
    print('access not granted')
    password = input('Enter password: ')
print('Access granted')


import random
rounds = 0
total_rolls = 0

while rounds <= 100000:
    dice1 = dice2 = rolls = 0
    while dice1!=6 or dice2!=6:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls = rolls + 1
    rounds = rounds + 1
    total_rolls = total_rolls + rolls
average_rolls = total_rolls/rounds

print(f'Average rolls required: {average_rolls:6.2f}')

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f'{first} times {second} is {first*second:d}')
        second = second + 1
    first = first + 1

command = input('Enter command: ')
while command != 'stop':
    if command == 'MAYDAY':
        break
    print ('Exceuting command: ' + command)
    command = input('Enter command: ')
else:
    print('stop.')
print('Exceution stopped.')


