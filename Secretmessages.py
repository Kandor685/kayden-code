#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

encrypt_or_decrypt = input("Encrypt a message or decrypt a message? ")

if encrypt_or_decrypt == "encrypt" or encrypt_or_decrypt == "Encrypt":
    
    key = int(input("Enter How many spcaes forward the key should be: "))
    newMessage = ''

    message = input("Please Enter a Message: ")

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
            print(newMessage)
        else:
            newMessage += character

elif encrypt_or_decrypt == "decrypt" or encrypt_or_decrypt == "Decrypt":

    key = int(input("Enter How many spcaes backward the key should be: "))
    newMessage = ''

    message = input("Please Enter a Message: ")

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
            print(newMessage)
        else:
            newMessage += character
else:
    print("ERROR: Invalid input! Goodbye!")