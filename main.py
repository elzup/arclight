
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.900, auto_write=False, pixel_order=ORDER)
for i in range(num_pixels):
    pixels[i] = (0, 0, 0)
    if i % 20 == 0:
        pixels[i] = (100, 100, 0)
    elif i % 10 == 0:
        pixels[i] = (100, 0, 0)

pixels.show()
