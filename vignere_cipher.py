#vignere_cipher
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vignere(message,key,mode):
    amount = 0
    result = ''
    for letters in message:
        if letters.upper() in alpha:
            index = alpha.index(letters.upper())
            if mode == 'encrypt' : index += alpha.index(key[amount].upper())
            if mode == 'decrypt' : index -= alpha.index(key[amount].upper())
            index %= len(alpha)
            if letters.isupper() : result += alpha[index]
            if letters.islower() : result += alpha[index].lower()
            amount += 1
            if amount == len(key):
                amount = 0
        else:
            result += letters
    return result
def menu():
    option = input('\n\nDo you want to (e)ncrypt or (d)ecrypt : ')
    if option == 'e' : option = 'encrypt'
    else : option = 'decrypt'
    message = input('Enter your message : ')
    key = input('Enter your key : ')
    ciphertext = vignere(message,key,option)
    print('Encrypted: ' + ciphertext)
looping = True
while looping:
    try : menu()
    except : looping = False
    

    

        

        
