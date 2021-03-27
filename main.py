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
    
    if button_a.is_pressed():
        a_early = True
    else:
        a_early = False

	if button_b.is_pressed():
		b_early = True
	else:
		b_early = False
		
    while True:
        display.show(Image.CHESSBOARD)
        
        if button_a.is_pressed():
            if not a_early:
                winner = "A"
                break
        else:
            a_early = False
            
        if button_b.is_pressed():
            if not b_early:
                winner = "B"
                break
        else:
            b_early = False
            
    display.show(winner)
