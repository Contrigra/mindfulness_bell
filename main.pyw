import random
from time import sleep

from playsound import playsound
from pathlib import Path

while True:
    playsound(Path.cwd() / 'tibetan-bell-sound.mp3')
    sleep(random.randint(600, 1200))

