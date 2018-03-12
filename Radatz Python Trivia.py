##Midterm program
##ITCS 1950
##Developer: Sean Radatz
##Trivia Pursuit



import random
import time

question = list(range(40)) #list generation 1-40 integers
score = 0

def questrand(): #reverts score/ shuffles question order
    random.shuffle(question) #shuffle function within random, randomly shuffles all contents in question list
    global score
    score = 0
    text = open("Intro.txt", "r")
    stuff = text.read()
    print(stuff)
    time.sleep(2)
    

def questselect(): # goes through question order and calls proper fuction
#    print(question)
    for x in question:
        if x == 1:
            Ch1m()

        if x == 2:
            Ch2m()

        if x == 3:
            Ch3m()

        if x == 4:
            Ch4m()

        if x == 5:
            Ch5m()

        if x == 6:
            Ch6m()

        if x == 7:
            Ch7m()

        if x == 8:
            Ch8m()

        if x == 9:
            Ch9m()

        if x == 10:
            Ch10m()

        if x == 11:
            Ch11m()

        if x == 12:
            Ch12m()

        if x == 13:
            Ch13m()

        if x == 14:
            Ch14m()

        if x == 15:
            Ch15m()

        if x == 16:
            Ch16m()

        if x == 17:
            Ch17m()

        if x == 18:
            Ch18m()

        if x == 19:
            Ch19m()

        if x == 20:
            Ch20m()

        if x == 21:
            Ch1t()

        if x == 22:
            Ch2t()

        if x == 23:
            Ch3t()

        if x == 24:
            Ch4t()

        if x == 25:
            Ch5t()

        if x == 26:
            Ch6t()

        if x == 27:
            Ch7t()

        if x == 28:
            Ch8t()

        if x == 29:
            Ch9t()

        if x == 30:
            Ch10t()

        if x == 31:
            Ch11t()

        if x == 32:
            Ch12t()

        if x == 33:
            Ch13t()

        if x == 34:
            Ch14t()

        if x == 35:
            Ch15t()

        if x == 36:
            Ch16t()

        if x == 37:
            Ch17t()

        if x == 38:
            Ch18t()

        if x == 39:
            Ch19t()

        if x == 40:
            Ch20t()


########################################
#        Multiple choice questions     #
########################################


def Ch1m():
    handle = ''
    while handle == '':
        text = open("Ch1m.txt", "r") #opens text file
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'a' or answer == 'A':
            score = score + 50 # adds to score
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2) #timer to see score
            break
        else:
            print()
            print("I'm sorry the answer was A...")
            print()
            time.sleep(2)
            break

def Ch2m():
    handle = ''
    while handle == '':
        text = open("Ch2m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch3m():
    handle = ''
    while handle == '':
        text = open("Ch3m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch4m():
    handle = ''
    while handle == '':
        text = open("Ch4m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch5m():
    handle = ''
    while handle == '':
        text = open("Ch5m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch6m():
    handle = ''
    while handle == '':
        text = open("Ch6m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch7m():
    handle = ''
    while handle == '':
        text = open("Ch7m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'a' or answer == 'A':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was A...")
            print()
            time.sleep(2)
            break

def Ch8m():
    handle = ''
    while handle == '':
        text = open("Ch8m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'a' or answer == 'A':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was A...")
            print()
            time.sleep(2)
            break

def Ch9m():
    handle = ''
    while handle == '':
        text = open("Ch9m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch10m():
    handle = ''
    while handle == '':
        text = open("Ch10m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch11m():
    handle = ''
    while handle == '':
        text = open("Ch11m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch12m():
    handle = ''
    while handle == '':
        text = open("Ch12m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch13m():
    handle = ''
    while handle == '':
        text = open("Ch13m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch14m():
    handle = ''
    while handle == '':
        text = open("Ch14m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch15m():
    handle = ''
    while handle == '':
        text = open("Ch15m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch16m():
    handle = ''
    while handle == '':
        text = open("Ch16m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'a' or answer == 'A':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was A...")
            print()
            time.sleep(2)
            break

def Ch17m():
    handle = ''
    while handle == '':
        text = open("Ch17m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'b' or answer == 'B':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was B...")
            print()
            time.sleep(2)
            break

def Ch18m():
    handle = ''
    while handle == '':
        text = open("Ch18m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

def Ch19m():
    handle = ''
    while handle == '':
        text = open("Ch19m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'a' or answer == 'A':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was A...")
            print()
            time.sleep(2)
            break

def Ch20m():
    handle = ''
    while handle == '':
        text = open("Ch20m.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'c' or answer == 'C':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was C...")
            print()
            time.sleep(2)
            break

########################################
#        True/False questions          #
########################################

def Ch1t():
    handle = ''
    while handle == '':
        text = open("Ch1t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch2t():
    handle = ''
    while handle == '':
        text = open("Ch2t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch3t():
    handle = ''
    while handle == '':
        text = open("Ch3t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch4t():
    handle = ''
    while handle == '':
        text = open("Ch4t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch5t():
    handle = ''
    while handle == '':
        text = open("Ch5t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch6t():
    handle = ''
    while handle == '':
        text = open("Ch6t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch7t():
    handle = ''
    while handle == '':
        text = open("Ch7t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch8t():
    handle = ''
    while handle == '':
        text = open("Ch8t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch9t():
    handle = ''
    while handle == '':
        text = open("Ch9t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch10t():
    handle = ''
    while handle == '':
        text = open("Ch10t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch11t():
    handle = ''
    while handle == '':
        text = open("Ch11t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch12t():
    handle = ''
    while handle == '':
        text = open("Ch12t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch13t():
    handle = ''
    while handle == '':
        text = open("Ch13t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch14t():
    handle = ''
    while handle == '':
        text = open("Ch14t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch15t():
    handle = ''
    while handle == '':
        text = open("Ch15t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 't' or answer == 'T':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was True...")
            print()
            time.sleep(2)
            break

def Ch16t():
    handle = ''
    while handle == '':
        text = open("Ch16t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch17t():
    handle = ''
    while handle == '':
        text = open("Ch17t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch18t():
    handle = ''
    while handle == '':
        text = open("Ch18t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch19t():
    handle = ''
    while handle == '':
        text = open("Ch19t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def Ch19t():
    handle = ''
    while handle == '':
        text = open("Ch19t.txt", "r")
        stuff = text.read()
        global score
        print()
        print(stuff)
        answer = input()
        if answer == 'f' or answer == 'F':
            score = score + 50
            print()
            print('Congratulations you just won 50 points!!!!')
            print()
            time.sleep(2)
            break
        else:
            print()
            print("I'm sorry the answer was False...")
            print()
            time.sleep(2)
            break

def grade(value): #Displays score
    value = str(value)
    print()
    print("Congratulations you have won " + value + ' points!!!!')
    print()
    time.sleep(2)


########################################
#                 Main                 #
########################################

def main():
    game = 'yes'
    while game == 'yes' or game == 'y':

        questrand()

        questselect()

#        print(score)
        grade(score)

        print('Would you like to play again? Y\\N?')
        game = input()

main()
