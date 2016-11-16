# ftma
A new multiplayer game, based in medieval times. The library is written in Python using mainly our own libs and sockets.

# Installation and Setup


### Ubuntu/Debian

In terminal, download the repo and enter that directory: 

``` bash
git clone https://github.com/ffd/ftma-game.git
cd ftma-game
```

Then, install the needed dependencies from the apt repos: 

```sudo apt-get install python-virtualenv python3```

Next, create a python virtual environment, activate it, and install the needed python dependencies:

```bash
virtaulenv -p python3 .venv
source .venv/bin/activate
pip3 install pygame 
```

Then start the game:

``` bash
python3 main.py
```

### Mac OS (Untested)

First install the needed dependencies: 

``` bash
brew install python3 git
pip install virtualenv
```

Then, download the repo and enter that directory: 

``` bash
git clone https://github.com/ffd/ftma-game.git
cd ftma-game
```

Next, create a python virtual environment, activate it, and install the needed python dependencies:

```bash
virtaulenv -p python3 .venv
source .venv/bin/activate
pip3 install pygame 
```

Then start the game:

``` bash
python3 main.py
```

# Styleguide:
1. Default data type will be dicts
2. Origin will be in the bottom left

# Packages Currently Used:
 - Pygame - for keyboard polling

# Game Vision

### Gameplay
 - Top-down 2.5D
 - Encounter based combat
 - Built and balanced around a 4 person party (not limited to)
 

### Character Design
 - Trait system - Repeated action leads to strength / weakness
 - Class system - Heavy interaction
   - Fighter - frontlines
     - Knight - high armor
     - Warrior - balanced
     - Berzerker - high dps
   - Thief - high dps, squishy
     - Assassin - extremely high dps
     - Trapper - set traps
   - Mage - enhancement
     - Elemental - ranged, fire/ice/earth
     - Arcane - melee, blink, shield
     - Priest - shadow - enemy debuffs, light - party buffs
   - Archer - backlines
     - Handler- pets, etc.
     - Heavy - charge attack
     - Support - camps + healing

### Enemies
 - Behaviors
   - Rush
   - Guarded
   - Stationary
   - Kiting
   - Arbitrary
 - Types
   - Trash - weak, low dps, many
   - Elite - stronger, average dps, rallies small enemies
   - Boss - one per room, one or two per level

### Narrative/ Environment
 - Rooms - discrete fighting areas
   - Characteristics - factor into strengths based on class and specialty
     - Lighting
     - Layout
     - Weather
     - Location
     - Time of day
   - Thematically sensible enemies

### Setting
 - Medieval
 - Varied mood / gameplay

### Graphics
 - Voxel based

# Technologies (game engine)
### Single player
1. Poll input
   - for controller in playerlist get buttonstate
2. Advance game state
   - Advance player
   - Advance interactables (spells, projectiles, persistence effects, traps, etc)
   - Advance enemies
   - Advance environment (particle effects, misc animations)
3. Render game state

### Multiplayer
1. Server requests input
2. Clients send input
3. Host advances game state
4. Host sends back gamestate
5. Clients render game

# Data Definitions:
### World:
 - Room
 - List of players
 - List of interactables
 - List of enemies (mobs)
 - List of scene elements

### Room
 - Layout - matrix of block IDS
 - Tileset - array of block sprites at tileset[ID]

*later we should cache the level image so we don’t have to re-render it

### Player data
 - movement information
 - class
 - stats
 - statuses and modifiers (buffs, debuffs, crowd control)
 - gear (updated at closing inventory)
 - skills (updated at leveling/specing)

### Intractable data (all items that need collision checking)
 - movement information
 - size
 - status effects
 - persistence (0 for infinite, 1 for simple, >1 for piercing)
 - sprite
 - frames left

### Enemy data
 - movement information
 - stats
 - sprite
 - behavior

### Environment data
 - Location
 - Frame (decrements, deletes at 0)
 - Base file
