user = input('Try to guess the number between 1-100: ')

def script():
    user = input('Try to guess the number again: ')
    if int(user) > x:
        print('\033[1m''You are a way too higher. The number is smaller than your guess''\033[0m')
        script()
    elif int(user) <x:
        print('\033[1m''You are a way too lower. The number is bigger than your guess''\033[0m')
        script()
    elif int(user) == x:
        print('\033[1m''You have guessed it right!!''\033[0m')
        quit()
script()

