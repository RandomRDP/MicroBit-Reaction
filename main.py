from microbit import *


while True:

	while not button_a.is_pressed() or not button_b.is_pressed():
		pass
    
    for i in range(3, 0, -1):
        music.play( ["b5:1"] )       
        display.show("{}".format(i))
        utime.sleep(1)
	
    display.clear()
    music.play( music.BA_DING )