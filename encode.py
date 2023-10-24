# Sebastian Dion
def encode(password):
    encopass = ''
    for i in password:
        encopass += str((int(i) + 3) % 10)
    return encopass