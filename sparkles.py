from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

while True:
    #think of random number between 0 and 7 for x and y
    x = randint(0, 7)
    y = randint(0, 7)
        #RGB Color Scale (0-255)
    r = 0
    g = 0
    b = 0
    sense.set_pixel(x, y, r, g, b)
    sleep(0.1)

    
