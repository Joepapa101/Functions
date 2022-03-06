y = ''
sales = 0
looping = 0
user = input('Do you want to sell a ticket?  (y/n):')
while looping == 0:
    if user == 'y':
        print('A for adult')
        print('S for student')
        print('C for child')
        print('G for gift voucher')
        type_of_ticket = input('What type of ticket do you want?:')
        if type_of_ticket == 'A':
            sales += 12.5
        elif type_of_ticket == 'S':
            sales += 9
        elif type_of_ticket == 'C':
            sales += 7
        elif type_of_ticket == 'G':
            print('Gift voucher is free')
        else:
            print('Nice try buster')
        loop = input('Would you like another ticket(y/n)')
        if loop == 'y':
            looping == 0
        elif loop == 'n':
            looping += 1
print(f'The total price is {sales}')

