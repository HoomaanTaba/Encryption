# Allameh Helli 10 high school
# Programming class
# HelliPaad
# HoomaanTaba

from random import randint
import os

# changing the color of text
os.system('color A')

# ROT13 function
def rot13(ar):
    for i in range(len(ar)):
        if ord(ar[i]) >= ord('A') and ord(ar[i]) <= ord('M'):
            ar[i] = chr(ord(ar[i])+13)
        elif ord(ar[i]) > ord('M') and ord(ar[i]) <= ord('Z'):
            ar[i] = chr(ord(ar[i])-13)
        elif ord(ar[i]) >= ord('a') and ord(ar[i]) <= ord('m'):
            ar[i] = chr(ord(ar[i])+13)
        elif ord(ar[i]) > ord('m') and ord(ar[i]) <= ord('z'):
            ar[i] = chr(ord(ar[i])-13)
        elif ord(ar[i]) >= ord('0') and ord(ar[i]) < ord('5'):
            ar[i] = chr(ord(ar[i])+5)
        elif ord(ar[i]) >= ord('5') and ord(ar[i]) <= ord('9'):
            ar[i] = chr(ord(ar[i])-5)
print("Hello! Welcome to our encryption software!")
while True:
    print('''
If you want to encrypt a text, enter E.
If you wnat to decrypt a text, enter D.\n''')

    dcd = input()
    if dcd == 'e' or dcd == 'E' or dcd == 'd' or dcd == 'D':
        # inputing the name of file
        name = input("Enter your file name: ")
        # *** In this part, you must type your own desktop address. ***
        ad = r"C:\\Users\\Ali\\Desktop\\" + name + ".txt"
    else:
        print("Please enter E or D.")
        quit()
        
    # Encryption part
    if dcd == 'e' or dcd == 'E':
        # inputing the text
        inp = input("Do you wnat to type it or import a file? (T or I): ")
        if inp == 'T' or inp == 't':
            text = input("Type your text or press Ctrl + V if you have copied the text: ")
        elif inp == 'I' or inp == 'i':
            file = open(ad,"r")
            text = file.read()
            file.close()
        else:
            print("Please enter T or I in this part.\n")
        
        new = []
        
        # Reverse algorithm
        for i in range(len(text)):
            new += (text[len(text)- i - 1])
            
        # Rot13 algorithm
        rot13(new)
                
        # random algoritm and write in the file
        file = open(ad,"w")
        for i in range(len(new)):
            file.write(new[i])
            file.write(chr(randint(33,96)))
            file.write(chr(randint(33,96)))
        file.close()
        print("Your file is in Desktop. Goodluck!\n")

    # Decryption part
    elif dcd == 'd' or dcd == 'D':
        # opening the file
        try:
            file = open(ad,"r")
            text = file.read()
            file.close()
            new = []
        except FileNotFoundError:
            print("This file doesn't exist in Desktop!\n")
            quit()

        # decrypt random algorithm
        for i in range(len(text)):
            if i % 3 == 0:
                new.append(text[i])
                
        # decrypt reverse algorithm
        new.reverse()

        # decrypt ROT13 algorithm
        rot13(new)

        # Writing in file
        inp = input("Do you want to decryot privious file? (Y or N): ")
        if inp == 'Y' or inp == 'y':
            file = open(ad, "w")
            for i in range(len(new)): file.write(new[i])
            file.close()
            print("Your file is in Desktop. Goodluck!\n")
        elif inp == 'N' or inp == 'n':
            nad = r"C:\\Users\\Ali\\Desktop\\" + name + " (encrypted).txt"
            nfile = open(nad, "w")
            for i in range(len(new)): nfile.write(new[i])
            nfile.close()
            print("Your file is in Desktop. Goodluck!\n")
        else:
            print("Please enter Y or N in this part.")
            quit()
