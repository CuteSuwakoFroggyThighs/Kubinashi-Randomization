from python_ini.ini_writer import IniWriter
import random
from array import array

w = IniWriter()

#Defines all possible stage numbers for sorting
stages = array('b', [30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88])

#Characters sorted by number (0 = Seki, 1 = Rumia, 2 = Cirno, 3 = Seija)
characters = array('b', [0, 1, 2, 3])

#Stage randomization
while True:
    try:
        changestage = input("Would you like to randomize the stage order? (Yes/No): ")
        includestages = str(changestage)
        if includestages.lower() in ("yes", "no"):
            break
        else:
            print("A simple Yes or No will suffice.")
    except ValueError:
        print("A simple Yes or No will suffice.")

#Character randomization
while True:
    try:
        changeplayer = input("Would you like to randomize the characters? (Yes/No): ")
        includeplayer = str(changeplayer)
        if includeplayer.lower() in ("yes", "no"):
            break
        else:
            print("A simple Yes or No will suffice.")
    except ValueError:
        print("A simple Yes or No will suffice.")

#choice of character without randomization
if includeplayer.lower() in ("no"):
    while True:
        try:
            playerchoice = input("Which character would you like to play? 'D' for Default, 'S' for Sekibanki, 'R' for Rumia, 'C' for Cirno, 'Sj' for Seija: ")
            selectplayer = str(playerchoice)
            if selectplayer.lower() in ("d"):
                break
            if selectplayer.lower() in ("s"):
                chosenplayer = str(0)
                break
            if selectplayer.lower() in ("r"):
                chosenplayer = str(1)
                break
            if selectplayer.lower() in ("c"):
                chosenplayer = str(2)
                break
            if selectplayer.lower() in ("sj"):
                chosenplayer = str(3)
                break
            else:
                print("Please select a character.")
        except ValueError:
            print("Please select a character.")


#ask about adding omake stages to the pool
while True:
    try:
        omake = input("Would you like omake password stages to be affected? (Yes/No): ")
        includeomake = str(omake)
        if includeomake.lower() in ("yes"):
            stages.fromlist([93, 94, 95, 96, 97, 98, 99])
            break
        elif includeomake.lower() in ("no"):
            break
        else:
            print("A simple Yes or No will suffice.")
    except ValueError:
        print("A simple Yes or No will suffice.")

#ask about adding other character stages to the pool
while True:
    try:
        alternate = input("What about other character stages? (Yes/No): ")
        includealternate = str(alternate)
        if includealternate.lower() in ("yes"):
            stages.fromlist([104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 119, 120, 121, 122, 123])
            break
        elif includealternate.lower() in ("no"):
            break
        else:
            print("A simple Yes or No will suffice.")
    except ValueError:
        print("A simple Yes or No will suffice.")
        
#ask for seeding or lack of seeing
while True:
    try:
        seeded_input = input("Do you want a seeded run? Yes or No: ")
        seeded = str(seeded_input)
        if seeded.lower() in ("yes", "no"):
            break
        else:
            print("A simple Yes or No will suffice.")
    except ValueError:
        print("A simple Yes or No will suffice.")


#Using earlier input, now we determine the randomization structure
if seeded.lower() in ("yes"):
    generationseed = input("What would you like to use for a seed? (Input should be a string): ")
    finalseed = str(generationseed)
    random.seed(finalseed)
    random.shuffle(stages)
elif seeded.lower() in ("no"):
    random.shuffle(stages)

#Asking now for which save file to write to
while True:
    try:
        file = input("Which file do you wish to use? (1-3): ")
        filenumber = str(file)
        if filenumber in ("1","2","3"):
            break
        else:
            print("Only 1-3 can be selected")
    except ValueError:
        print("Only numbers please")
savefile = "data"+filenumber+"."+"sav"

#Function to write each set of stages or characters as needed, because this needs to happen 10 times total
def eachworld():
    if includestages.lower() in ("yes"):
        w.key('levelOne', str(stages.pop(-1)))
        w.key('levelTwo', str(stages.pop(-1)))
        w.key('levelThree', str(stages.pop(-1)))
        w.key('levelFour', str(stages.pop(-1)))
        w.key('levelFive', str(stages.pop(-1)))
    if includeplayer.lower() in ("yes"):
        w.key('cOne', random.choice(characters))
        w.key('cTwo', random.choice(characters))
        w.key('cThree', random.choice(characters))
        w.key('cFour', random.choice(characters))
        w.key('cFive', random.choice(characters))
    if includeplayer.lower() in ("no") and selectplayer.lower() in ("s", "c", "r", "sj"):
        w.key('cOne', str(chosenplayer))
        w.key('cTwo', str(chosenplayer))
        w.key('cThree', str(chosenplayer))
        w.key('cFour', str(chosenplayer))
        w.key('cFive', str(chosenplayer))

#It's time for the fun, ini file writing. This will be utter chaos, buckle up.
w.section('stageOne')
eachworld()
w.section('stageTwo')
eachworld()
w.section('stageThree')
eachworld()
w.section('stageFour')
eachworld()
w.section('stageFive')
eachworld()
w.section('stageSix')
eachworld()
w.section('stageSeven')
eachworld()
w.section('stageEight')
eachworld()
w.section('stageNine')
eachworld()
w.section('stageTen')
eachworld()
if includeomake.lower() in ("yes"):
    w.section('omake')
    eachworld()
    if includestages.lower() in ("yes"):
        w.key('levelSix', str(stages.pop(-1)))
        w.key('levelSeven', str(stages.pop(-1)))
    if includeplayer.lower() in ("yes"):
        w.key('cSix', random.choice(characters))
        w.key('cSeven', random.choice(characters))
    if includeplayer.lower() in ("no") and selectplayer.lower() in ("s", "c", "r", "sj"):
        w.key('cSix', str(chosenplayer))
        w.key('cSeven', str(chosenplayer))
if includealternate.lower() in ("yes"):
    w.section('stageRumia')
    eachworld()
    w.section('stageCirno')
    eachworld()
    if includestages.lower() in ("yes"):
        w.key('levelSix', str(stages.pop(-1)))
        w.key('levelSeven', str(stages.pop(-1)))
    if includeplayer.lower() in ("yes"):
        w.key('cSix', random.choice(characters))
        w.key('cSeven', random.choice(characters))
    if includeplayer.lower() in ("no") and selectplayer.lower() in ("s", "c", "r", "sj"):
        w.key('cSix', str(chosenplayer))
        w.key('cSeven', str(chosenplayer))
    w.section('stageSeija')
    eachworld()

w.write(savefile)

print('In order to use the randomizer, drop the newly created save file into %localappdata%\DullahanRecollection')
