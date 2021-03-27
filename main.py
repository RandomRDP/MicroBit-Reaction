from microbit import *
from random import *
import utime
import music

MIN_TIME = const(1 * 1000)
MAX_TIME = const(10 * 1000)

while True:

    while not button_a.is_pressed() or not button_b.is_pressed():
        pass
    
    for i in range(3, 0, -1):
        music.play( ["b5:1"] )       
        display.show("{}".format(i))
        utime.sleep(1)

    display.clear()    
    music.play( music.BA_DING )
    utime.sleep_ms(randint(MIN_TIME, MAX_TIME))
    
    while True:
        if button_a.is_pressed():
            winner = "A"
            break
        display.show(Image.CHESSBOARD)
        
        if button_b.is_pressed():
            winner = "B"
            break
    display.show(winner)