from itertools import product

user = input('What is your name?')
print('Hello ' + user + '!')
H = input('Whats the radius of the circle?')
pi = 3.14159
radius = float(H)
area = pi * radius * radius
print('The area of the circle is', area)

length = float(input('What is the length of a rectangle? '))
width = float(input('What is the width of a rectangle? '))
area = length * width
print('The area of the rectangle is', area)
perimeter = 2*length + 2*width
print('The perimeter of the rectangle is', perimeter )

number_one = int(input('choose a number?'))
number_two = int(input('choose another number?'))
number_three = int(input('choose another number?'))
sum = number_one + number_two + number_three
product = number_one * number_two * number_three
average = sum / 3
print('The average is', average)
print('The sum is', sum)
print('The product is', product)

talents1 = int(input('Enter talents?'))
pounds1 = int(input('Enter pounds?'))
lots1 = float(input('Enter lots?'))
lots_from_talents = talents1 * 20 * 32
lots_from_pounds = pounds1 * 32
total_lots = lots_from_talents + lots_from_pounds + lots1
total_grams = total_lots * 13.3
kilograms = total_grams // 1000
grams = total_grams % 1000
print('The weigth in modern units')
print(f'The mass is {kilograms} kilograms and {grams:.2f} grams.')

import random
three_digits_first= random.randint(0,9)
three_digits_second= random.randint(0,9)
three_digits_third= random.randint(0,9)

four_digits_first= random.randint(1,6)
four_digits_second= random.randint(1,6)
four_digits_third= random.randint(1,6)
five_digits_fourth= random.randint(1,6)

print(f'3-digit code: {three_digits_first}{three_digits_second}{three_digits_third}')
print(f'4-digit-code: {four_digits_first}{four_digits_second}{four_digits_third}{five_digits_fourth}')