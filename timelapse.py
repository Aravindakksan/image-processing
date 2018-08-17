
import os
import time

FRAMES = 1000
TIMEBETWEEN = 28800

frameCount = 0
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(7)
    os.system("raspistill -o image%s.jpg"%(imageNumber))
    frameCount += 1
    time.sleep(TIMEBETWEEN - 28800) #Takes roughly 8 hours to take a picture
