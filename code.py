import board
import digitalio
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
delay = .25
print("Hello World!")

while True:
    time.sleep(delay)
    pixels.fill((255, 0, 0))
    time.sleep(delay)
    pixels.fill((0, 255, 0))
    time.sleep(delay)
    pixels.fill((0, 0, 255))
    time.sleep(delay)
    pixels.fill((255, 255, 0))
    time.sleep(delay)
    pixels.fill((255, 0, 255))
    time.sleep(delay)
    pixels.fill((0, 255, 255))

