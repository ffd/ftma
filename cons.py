
### for creating objects

from enum import Enum

class Class(Enum):
    fighter = 1
    theif   = 2
    mage    = 3
    archer  = 4

def createRoom(layout, tileset):
    return {'layout' : layout,  # matrix of tiles by tileset index
            'tileset': tileset  # art for tiles used in layout
            }

def createWorld(room, plist, ilist, mobs, scene):
    return {'room'  : room,  # current room
            'plist' : plist, # playerlist
            'ilist' : ilist, # interactablelist
            'mobs'  : mobs,  # monsters
            'scene' : scene  # non-interactable scene elements
            }

def createPlayer(x, y, z, pmag, pdir, vmag, vdir, accel, maxs, f):
    return {'x' : x, # x co-ord
            'y' : y, # y co-ord
            'z' : z, # z co-ord
            'pmag' : p, # momentum magnitude
            'pdir' : p, # momentum direction
            'vmag' : v, # velocity magnitude
            'vdir' : v, # velocity direction
            'accel' : accel, # acceleration
            'maxs' : maxs, # max speed
            'f' : f # friction
            }
