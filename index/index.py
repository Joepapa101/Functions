def check_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Chungus(Solomon)'
    else:
        print('ur thic')
user = int(input('How much do you weigh: '))
print(check_bmi)