#!/usr/bin/env python
# Display a runtext with double-buffering.
from editbase import EditBase
from rgbmatrix import graphics
import time
import random
import RPi.GPIO as GPIO

cnl = 18
GPIO.setmode(GPIO.BOARD)

docstat = 'In'

class RunText(EditBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def Run(self):
        if docstat == 'In':
            status = 'Doc is IN'
        if docstat == 'Out':
            status = 'Doc is OUT'

        offscreenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/rgb-led-array-stuff/fonts/7x13.bdf")
        randomRed = random.randint(0,255)
        randomBlue = random.randint(0,255)
        randomGreen = random.randint(0,255)
        textColor = graphics.Color(randomRed, randomBlue, randomGreen)
        pos = offscreenCanvas.width
        #myText = time.strftime ('%l:%M%p')#self.args["text"]
        height = random.randint(10,32)

        while True:
            offscreenCanvas.Clear()
            len = graphics.DrawText(offscreenCanvas, font, pos, height, textColor, time.strftime ('%l:%M %p %b %d')); graphics.DrawText(offscreenCanvas, font, pos, height+10, textColor, status)
            pos -= 1
            if (pos + len < 0):
                pos = offscreenCanvas.width
                height = random.randint(10,32)
                randomRed = random.randint(0,255)
                randomBlue = random.randint(0,255)
                randomGreen = random.randint(0,255)
                textColor = graphics.Color(randomRed, randomBlue, randomGreen)

            time.sleep(0.10)
            offscreenCanvas = self.matrix.SwapOnVSync(offscreenCanvas)


# Main function
if __name__ == "__main__":
    parser = RunText()
    if (not parser.process()):
        parser.print_help()
if KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting')
