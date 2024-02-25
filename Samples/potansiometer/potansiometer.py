from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(32))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    pot_res = pot.read()
    print(pot_res)
    sleep(0.2)