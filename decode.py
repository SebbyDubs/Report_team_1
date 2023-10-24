# Gabriel Lemus
def decode(password):
    decoded_pass = ''
    for char in password:
        if int(char) - 3 == -3:
            decoded_pass += '7'
        elif int(char) - 3 == -2:
            decoded_pass += '8'
        elif int(char) - 3 == -1:
            decoded_pass += '9'
        else:
            decoded_pass += str(int(char) - 3)
    return decoded_pass
