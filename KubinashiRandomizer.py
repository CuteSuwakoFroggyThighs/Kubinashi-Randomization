from python_ini.ini_writer import IniWriter
import random
from array import array

w = IniWriter()

#Defines all possible stage numbers for sorting
stages = array('b', [30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88])


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
        print("What? Go back")


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

#Function to write each set of stages as needed, because this needs to happen 10 times total
def eachworld():
    w.key('levelOne', str(stages.pop(-1)))
    w.key('levelTwo', str(stages.pop(-1)))
    w.key('levelThree', str(stages.pop(-1)))
    w.key('levelFour', str(stages.pop(-1)))
    w.key('levelFive', str(stages.pop(-1)))

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

w.write(savefile)

print('''In order to use the randomizer, drop the newly created save file into %localappdata%\DullahanRecollection''')
