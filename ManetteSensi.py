from microbit import *
import music
import neopixel

# Initialise neopixels
npix = neopixel.NeoPixel(pin13, 6)

# Define some colours
red = (64 , 0, 0)
green = (0, 64, 0)
blue = (0, 0, 64)
nocol = (0, 0, 0)

# light all neopixels with given colour
def light_all(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()

# wipe a colour across pixels one at a time
def wipe(col, delay):
    for pix in range(0, len(npix)):
        npix[pix] = col
        npix.show()
        sleep(delay)

def read_joy():
    return pin1.read_analog(), pin2.read_analog(), pin8.read_digital()

def read_buttons():
    # red, blue, green, yellow
    btns = [pin12, pin15, pin14, pin16]
    return [p.read_digital() for p in btns]

def read_pot():
    return pin0.read_analog()

def play_tune():
    music.play(music.BADDY)
    pin0.read_digital()


light_all(red)
play_tune()
wipe(blue, 250)
while True:
    x, y, j = read_joy()
    btns = read_buttons()
    p = read_pot()
    print(x, y, j, btns, p)
    sleep(20)
