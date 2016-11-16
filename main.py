# packages
from time import time, sleep

# local imports
from cons import createRoom, createWorld, createPlayer
from keyboard import KeyPoller, getKeys

# globals
TPS      = 1
INTERVAL = 1 / TPS


def tick():
    with KeyPoller() as keyPoller:
        last_called = time()

        while True:
            """
            c = keyPoller.poll()
            if not c is None:
                if c == "c":
                    break
                print repr(c)
            """
            getKeys()

            TTS = INTERVAL - (time() - last_called)
            if TTS > 0:
                sleep(TTS)
            last_called = time()


def main():
    tick()






main()



player1 = createPlayer(0, 0, 0, 0, 0, 0, 0, 2, .1)
