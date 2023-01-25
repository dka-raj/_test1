from random import randint, choice
import pyttsx3
from time import sleep
from os import system


def cls(): return system("clear")


tts = pyttsx3.init()
del pyttsx3
tts.setProperty("voice", "english-us")
tts.flag = True
digits = [3, 4, 6, 7, 8]
number_of_questions = 10
speed = 170
specific = False
wait = False
last = "👉  Give Direct answers  👈"


def setting():
    global number_of_questions, speed, specific,  wait
    # number_of_questions
    inp = input(F"Number of questions(def: {number_of_questions}) : ")
    if inp != "":
        number_of_questions = int(inp)

    # speed
    inp = input(F"% tts Speed(def:{speed}%) : ")
    if inp != "":
        speed = int(inp)
        tts.flag = tts.setProperty(
            "rate", speed*2) if not speed == 0 else False

    # specific
    inp = input(
        F"Specific numbers(def: {'random' if not specific else specific}) : ")
    if inp != "":
        specific = inp.split(" ")

    # sleep
    inp = input(
        F"Wait Time in Seconds(def: {'User Dependent' if not wait else wait}) : ")
    if inp != "":
        wait = float(inp)
    return True


def ready() -> bool:
    inp = input("🏁  ")
    if inp == "":
        return True
    elif inp == "]":
        return setting()
    else:
        return False


def main(specificNO=False):
    global last
    for i in range(1, number_of_questions+1):
        number1 = randint(31, 99)
        number2 = specificNO if specificNO else choice(digits)
        product = number1*number2
        text = f"{number1} x {number2}"
        cls()
        print(last)
        print(text, end="")
        sleep(wait) if wait else input()
        ans = str(product)
        last = ans+"👇"
        if tts.flag != False:
            tts.say(" ".join(digit for digit in ans.replace("0", "o")))
            tts.runAndWait()


setting()
while ready():
    if not specific:
        main()
    else:
        for specificNO in specific:
            main(int(specificNO))
    print(last)
