import RPi.GPIO as gpio
import time
import random

gpio.setmode(gpio.BCM)

leds = [21, 12, 16, 12, 7, 8, 25, 24]

gpio.setup(leds, gpio.OUT)

def garland(leds):
    for i in range(len(leds)):
        if i == 0:
            gpio.output((leds[-1], leds[i]), (0, 1))
        else:
            gpio.output(leds[i-1:i+1], (0, 1))
        time.sleep(0.2)

for i in range(3):
    garland(leds)

gpio.output(leds, 0)
gpio.cleanup()

def bin_volt(channels, number):
    gpio.output(channels, list(f'{number:b}'))

dac = [26, 19, 13, 6, 5, 11, 9, 10]

number = [random.choice([0, 1]) for _ in range(len(dac))]
print(number)

gpio.setup(dac, gpio.OUT)

gpio.output(dac, number)

time.sleep(15)

bins = [2, 255, 127, 64, 32, 5, 0, 256]

for i in bins:
    bin_volt(dac, i)
    _ = input()

gpio.output(dec, 0)

gpio.cleanup()

def au(inp, out):
    ou = []
    for i in inp:
        ou.append(gpio.input(i))
    gpio.output(out, ou)

aux = [22, 23, 27, 18, 15, 14, 3, 2]

gpio.setup(leds, gpio.OUT)

gpio.setup(aux, gpio.IN)

while True:
    au(aux, leds)