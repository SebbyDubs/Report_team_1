from encode import encode
from decode import decode

def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    user_input = input('Please enter an option: ')
    return int(user_input)

password = ''


if __name__ == '__main__':
    while True:
        inp = main()
        if inp == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif inp == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
            print()
        elif inp == 3:
            exit()
        else:
            continue

