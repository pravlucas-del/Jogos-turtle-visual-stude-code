from random import *
from pygame import *
import sys


init()
puc_image = image.load("puc.png")
window = display.set_mode((1280,720))

display.set_caption("Resgate do Bicalho")

window.fill((135,206,235))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    window.fill((255,255,255))
    window.blit(puc_image,(300,210))
    
