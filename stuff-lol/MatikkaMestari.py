# (c) Hassunaama 2022 All Rights Reserved.
import os


number = 1
while True:
    print("Mikä on: " + str(number) + "+" + str(number))
    f = open("highscore.txt", "r")
    if(number >= int(f.read())):
        f = open("highscore.txt", "w")
        f.write(str(number))
        f.close()
    else:
        pass

    answer = input("Vastaus: ")

    if(number + number == int(answer)):
        number = int(answer)
        os.system('cls')
    else:
        print("Väärin!")
        break

f = open("highscore.txt", "r")
print("Sinun paras tuloksesi on: " + f.read() + ", Sinun tämän kertainen tulos oli: " + str(number) + "!")
os.system('pause')
