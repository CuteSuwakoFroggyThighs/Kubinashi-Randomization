# Kubinashi Randomization - A Kubinashi Recollection Randomizer -
<p align="center">
  <img src="/kubinashiRandomization.png">
</p>

### _Doremy Sweet, who was supposed to be fully managing the dream world, has gotten far too stressed out with the memory fragment incident. The once orderly dream world is now a complete mess. Locations mashed together, difficult challenges next to safe areas. Hopefully Sekibanki resolving this incident can bring the dream world back to order again._

[KubinashiRandomization Sample.webm](https://github.com/user-attachments/assets/0676d422-c2b4-4b9f-9bdc-b588b2b420d5)

# Features

- Randomized stage entrances
- Functional stage saving and loading
- Entirely possible to complete with 100% of achievements and S-Ranks
- Omake stages can be added to the pool of stages
- Alternate character stages given their own doors in the entrance (accessable by beating all 10 worlds)
- Alternate character stages can be added to the randomizer pool
- ALL CHARACTERS ON ALL STAGES
- Every character can obtain every puzzle piece and beat every stage
- Character choice can be randomized, or selected manually (selection is game-wide, I'm not masochistic enough to program per stage slection)
- Rumia cute

[RumiaTest-[00.00.000-00.25.279]-audio.webm](https://github.com/user-attachments/assets/f43aec9c-bc80-4f97-beab-da8179e13c84)


# Installation
Buy a copy of the game from Steam if you don't already own it. A steam copy is mandatory for the mod to work. [Kubinashi Recollection on Steam](https://store.steampowered.com/app/1635980/Kubinashi_Recollection/)

Download the mod from [Releases](https://github.com/CuteSuwakoFroggyThighs/Kubinashi-Randomization/releases)

#### 1. Extract the game's files from Game.exe using a program like WinRar or 7-Zip.
#### 2. Using Delta Patcher (https://github.com/marco-calautti/DeltaPatcher) or some variant of a xdelta patcher, patch the Game.win file from the newly extracted folder using the included .xdelta patch (this may require moving it outside the folder first if you have issues with Japanese characters in the file directory).
#### 3. Either copy steam_appid.txt from the release, or from the game's root directory and paste it into the extracted folder (this will allow the game to run).
#### 4. Run the included python script. The release features it pre-bundled as an executable so it requires no setup or installation, but the raw script itself will also work. 
#### 5. Move the created save file from the program/script's directory to %localappdata%/DullahanRecollection. 
#### 6. Either drag and drop the patched Game.win onto the extracted version of the game's executable (DullahanRecollection.exe), or run a powershell command in the folder like _"./DullahanRecollection.exe" "Game.win"_. Either way does the same thing, opening the modified Game.win with the executable. 
#### 7. Enjoy!

# Building / Inspecting Code

The python script is extremely simple, so there's not too much to specify. 
The script was written in Python 3.13.2, uses [Python_ini](https://github.com/ldthomas/python-ini), and was bundled as a standalone executable using [PyInstaller](https://github.com/pyinstaller/pyinstaller).

To analyze the changes made with the mod, apply the xdelta patch then use some form of [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) to open up the game's Data.win. There's far too many small changes to point out every single one, so you're on your own in exploration. 
If you wish to quickly look for what was changed, the mods apply mostly on save file loading, entering a stage, and stage completion.

# Issues
Probably going to be ignored. If suggestions or fixes pop up, I'll look into them, but that's all I can promise. Not much coding skill or GameMaker knowledge to work with here. 

# Future Ideas

~~The release will absolutely be updated some time in the next few days to include options for the Omake password stages. Currently they're not included due to a desire to finally publish the project.~~ Finished and implemented.

~~Possibly in the future, I'll look into including stages from Cirno, Rumia, and Seija's respective modes. That's a bit more work and will require adding doors to make sure the game is always possible to complete.~~ It's done. Playable Cirno, Seija, and Rumia are all here. 

~~Futher in the future, I may attempt adding character randomization. That will be a massive undertaking, as every stage will require a resouce allocation for each possible character, along with safe switching between everyone. We'll see.~~ Much pain was taken but the project is finished. 


# Credits 

[ぱらどっと](https://sekibanki.jp/) (Paradot) for developing this wonderful game I adore to no end.

[Pinky Cat](https://pinky-cat.github.io/) for information on editing stage loading.

UndertaleModTool and its various offshoots for making it even possible to work with GameMaker modding.

# Discredits

Dinner for being himself. 

