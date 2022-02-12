
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 10
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.900, auto_write=False, pixel_order=ORDER)
for i in range(num_pixels):
    pixels[i] = (255, 0, 0)
pixels.show()
