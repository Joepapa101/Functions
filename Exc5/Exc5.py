def check_factor(num1, num2):
    return num1 % num2


big = int(input('Enter a big number: '))
small = int(input('Enter a small number: '))
if check_factor(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is not a factor of {big}")