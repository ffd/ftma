# packages
from time import time, sleep

# local imports
from cons import createRoom, createWorld, createPlayer
from keyboard import getKeys

# globals
TPS      = 1
INTERVAL = 1 / TPS


def tick():

    getKeys()


def main():
    last_called = time()

    while True:

        tick()

        TTS = INTERVAL - (time() - last_called)
        if TTS > 0:
            sleep(TTS)
        last_called = time()







main()



player1 = createPlayer(0, 0, 0, 0, 0, 0, 0, 2, .1)
