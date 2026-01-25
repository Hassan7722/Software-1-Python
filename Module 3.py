length_of_zander = float(input("Please enter the length of zander in centimeters: "))

if length_of_zander >= 42:
    print('The zander meets the size limit.')
else:
    difference = 42 - length_of_zander
    print('The fish has been released back in to the lake')
    print('it was', difference , 'centimeters below the size limit.')

which_cabin_class = input("Please enter a cabin class: ")
if which_cabin_class == 'LUX':
    print('upper-deck cabin, equipped with a balcony. ')
elif which_cabin_class == 'A':
    print('above the car deck, equipped with a window. ')
elif which_cabin_class == 'B':
    print('windowless cabin above the car deck. ')
elif which_cabin_class == 'C':
    print('windowless cabin below the car deck. ')
else:
    print('Invalid cabin class. Please enter a valid cabin class. ')

biological_gender = str(input("Please enter your biological gender: "))
hemoglobin_value = int(input("Please enter the hemoglobin value (g/l): "))

if biological_gender == 'male':
    if hemoglobin_value < 117:
        print('The hemoglobin is low.')
    elif hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print('The hemoglobin is normal.')
    elif hemoglobin_value > 155:
        print('The hemoglobin is high.')

if biological_gender == 'female':
    if hemoglobin_value < 134:
        print('The hemoglobin is low.')
    elif hemoglobin_value >= 134 and hemoglobin_value <= 167:
        print('The hemoglobin is normal.')
    elif hemoglobin_value > 167:
        print('The hemoglobin is high.')
else:
    print('Invalid gender.')

year = int(input("Please enter the year: "))
if year / 400 == year // 400 :
    print('The year is a leap year. ')
elif year / 100 == year // 100 :
    print('The year is not a leap year. ')
elif year / 4 == year // 4:
    print('The year is a leap year. ')
else:
    print('The year is not a leap year. ')





