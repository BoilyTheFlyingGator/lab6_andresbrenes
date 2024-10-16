# Andres Brenes


def print_menu():

    print('\nMenu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')


def encode(data):
    encoded_data = ""
    for i in data:
        encoded_data += str(int(i) + 3)[-1]

    return encoded_data

def decode(data):
    s = ""
    for i in data[::-1]:
        if int(i)-3 < 0:
            s += str(10 + (int(i) - 3))
        else:
            s += str(int(i)-3)
    return s[::-1]


if __name__ == "__main__":

    option = 1

    while option != 3:

        print_menu()
        option = int(input('Please enter an option: '))

        match option:

            case 1:

                password = input('Please enter your password to encode: ')
                print('Your password has been encoded and stored!')

            case 2:
                print(f'The encoded password is {encode(password)}, and the original password is {decode(encode(password))}.')

            case 3:
                # option = 3
                exit()
            case _:
                pass

