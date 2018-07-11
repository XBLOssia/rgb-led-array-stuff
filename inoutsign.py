#!/usr/bin/env python
# Display a runtext with double-buffering.
from editbase import EditBase
from rgbmatrix import graphics
import time
import random
import RPi.GPIO as GPIO
import emoji


docstat = True

def switchdocstate(channel):
    global docstat
    docstat = not(docstat)
    global status

swtch = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(swtch,GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(swtch, GPIO.BOTH, switchdocstate, 600)



class RunText(EditBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def Run(self):
        
        status = 'On'

        offscreenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/rgb-led-array-stuff/fonts/7x13.bdf")
        fontTwo = graphics.Font()
        fontTwo.LoadFont("/home/pi/rgb-led-array-stuff/fonts/8x13.bdf")
        randomRed = random.randint(0,255)
        randomBlue = random.randint(0,255)
        randomGreen = random.randint(0,255)
        textColor = graphics.Color(randomRed, randomBlue, randomGreen)
        pos = offscreenCanvas.width
        #myText = time.strftime ('%l:%M%p')#self.args["text"]
        height = random.randint(10,22)
        emojistr = emoji.emojize(':tada: :sunrise: :bird: :cat: :alien: :volcano: :sunset: :tada:', use_aliases=True)

        while True:
            statustext = status
            offscreenCanvas.Clear()
            len = graphics.DrawText(offscreenCanvas, font, pos, height, textColor, time.strftime ('%l:%M %p %b %d')); graphics.DrawText(offscreenCanvas, font, pos+10, height+10, textColor, statustext); graphics.DrawText(offscreenCanvas, fontTwo, pos, height+20, textColor, emojistr)
            pos -= 1
            if (pos + len < 0):
                pos = offscreenCanvas.width
                height = random.randint(10,12)
                randomRed = random.randint(0,255)
                randomBlue = random.randint(0,255)
                randomGreen = random.randint(0,255)
                textColor = graphics.Color(randomRed, randomBlue, randomGreen)
                if docstat == True:
                    status = 'Doc is IN'
                if docstat == False:
                    status = 'Doc is OUT'
                statustext = status

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
