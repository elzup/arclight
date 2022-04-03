
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.900, pixel_order=ORDER)

pixels.fill((0, 0, 0))

# for i in range(num_pixels):
#    if i % 20 == 0:
#        pixels[i] = (100, 100, 0)
#    elif i % 10 == 0:
#        pixels[i] = (100, 0, 0)

pixels[100] = (100, 0, 0)
# pixels[200] = (100, 0, 0)

pixels.show()
