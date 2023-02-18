males = 0
females = 0

name = input("Name and Surname? ")

while name != 'ZZZ' and name != 'zzz':
    age = input('Age? ')
    gender = input("Gender? ")

    if gender == 'Male' or gender == 'male':
        males += 1

    elif gender == 'Female' or gender == 'female':
        females += 1

    print(name, age, gender)

    name = input("Name and Surname? ")

print(f'Male runners:{males}')
print(f'Female runners:{females}')

