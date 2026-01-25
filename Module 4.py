#1.
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1

#2.
ask_for_inches = float(input("Please enter a number in inches: "))

while ask_for_inches >= 0:
    centimeters = ask_for_inches * 2.54
    print(centimeters, 'centimeters')
    ask_for_inches = float(input("Please enter a number in inches: "))

#3.
number = input("Please enter a number: ")

if number != '':
    number = int(number)
    smallest = number
    largest = number

    while True:
        number = input("Please enter a number (empty to stop): ")
        if number == '':
            break
        number = int(number)

        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

print('The smallest number is ', smallest)
print('The largest number is ', largest)

#4.
import random

number =random.randint(1,10)
guess_number = int(input("Guess a number between 1 and 10: "))

while guess_number != number:
    if guess_number > number:
        print('Too high!')
    else:
        print('Too low!')
    guess_number = int(input("Guess again "))
print('Correct')

#5.
correct_username = 'python'
correct_password = 'rules'
attempts = 0

while attempts < 5:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == correct_username and password == correct_password:
        print('Correct')
        break
    else:
        print('Incorrect username or password')
        attempts = attempts + 1
if attempts == 5:
    print('Access denied')

#6
N = int(input("How many random points do u want to generate? "))

inside_circle = 0
total_points = 0

while total_points < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*y + y*y < 1:
        inside_circle = inside_circle + 1

    total_points = total_points + 1

pi = 4 * inside_circle / N
print('Approximation of pi:', pi)
