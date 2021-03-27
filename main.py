from microbit import *


while True:

	while not button_a.is_pressed() or not button_b.is_pressed():
		pass
    
    music.play( ["b5:1"] )       
    display.show("3")
    utime.sleep(1)
    music.play( ["b5:1"] )   
    display.show("2")
    utime.sleep(1)
    music.play( ["b5:1"] )      
    display.show("1")
    utime.sleep(1)
	
    display.clear()
    music.play( music.BA_DING )