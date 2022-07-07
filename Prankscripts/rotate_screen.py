# rotate screen twice
import time
import rotatescreen

screen = rotatescreen.get_primary_display()

for i in range(1, 9):
    screen.rotate_to(i*90 % 360)
    time.sleep(0.3)
