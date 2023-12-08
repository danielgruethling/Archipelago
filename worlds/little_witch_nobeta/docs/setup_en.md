# Little Witch Nobeta Multiworld Setup Guide

## Required Software

- [Little Witch Nobeta] (https://store.steampowered.com/app/1049890/Little_Witch_Nobeta/)Steam version of Little Witch Nobeta at the current version.
- [RandomizedWitchNobeta BepInEx mod](https://github.com/danielgruethling/RandomizedWitchNobeta/releases/tag/0.1.0-alpha)Download the LWNAP.zip from the github releases.

## Installation Procedures

This plugin modifies the game using [BepInEx](https://github.com/BepInEx/BepInEx), so it is needed to install BepInEx to load this plugin, here are the steps to achieve this:
- Find the installation directory of the game *(Usually in `steamapps/common`, you can find this from the game properties in steam -> local files -> browse...)*
- **/!\ Do a copy of your game installation and rename it `Little Witch Nobeta - Randomizer`** *(The changes are reversible but a pain to do, furthermore it's easier to have two versions of the game, one with the randomizer and the base one)*
- You should now have at least two folders in the `steamapps/common` directory: `Little Witch Nobeta` *(base game)* and `Little Witch Nobeta - Randomizer` *(will be modded with the Randomizer)*
- Download the randomizer: [**`LWNAP.zip`**](/../../releases/latest/download/LWNAP.zip)
- Copy all the files from the archive inside the game directory *(Where there is `LittleWitchNobeta.exe`)*
- Now you should see a file named `imgui.ini` just next to `LittleWitchNobeta.exe`
- Create a shortcut to `LittleWitchNobeta.exe`, name it as you want, run the game and enjoy!

A correct installation directory content should look like this:
```
.
├── BepInEx
├── dotnet
├── LittleWitchNobeta_Data
├── GameAssembly.dll
├── LittleWitchNobeta.exe
├── UnityCrashHandler64.exe
├── UnityPlayer.dll
├── baselib.dll
├── changelog.txt
├── doorstop_config.ini
├── imgui.ini
└── winhttp.dll
```

## Create a Config (.yaml) File

### What is a config file and why do I need one?

Your config file contains a set of configuration options which provide the generator with information about how it
should generate your game. Each player of a multiworld will provide their own config file. This setup allows each player
to enjoy an experience customized for their taste, and different players in the same multiworld can all have different
options.

### Where do I get a config file?

The [Player Settings](/games/Little%20Witch%20Nobeta/player-settings) page on the website allows you to configure
your personal settings and export a config file from them.

### Verifying your config file

If you would like to validate your config file to make sure it works, you may do so on the
[YAML Validator](/check) page.

### Joining a MultiWorld Game

When you join a multiworld game, you will be asked to provide your config file to whoever is hosting. Once that is done,
the host will provide you with a link to obtain the server information used to connect your game.

This can be split up into the following steps:

1. Navigate to the [Player Settings](/games/Little%20Witch%20Nobeta/player-settings) page, configure your options,
   and click the "Generate Game" button.
2. You will be presented with a "Seed Info" page.
3. Click the "Create New Room" link.
4. You will be presented with a server page, from which you can obtain the server information.
5. Start the game from the shortcut. It will load up an overlay menu when the main menu loads.
6. Tick the "Randomize using Archipelago" checkbox.
7. Insert the server information (hostname, port, slotname and password) in the fields.
8. Press the "Connect to Archipelago" button.
9. The settings should now autoadjust to the ones from your yaml.
10. Start a new run by clicking "New Randomizer" in the main menu or when reconnecting to a running session press "Resume Run" in the main menu.

### Play the game

When the game is connected, you're ready to begin playing. Congratulations on
successfully joining a multiworld game!
