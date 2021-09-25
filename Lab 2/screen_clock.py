import time
import subprocess
import digitalio
import board
import random
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from datetime import datetime

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
fontSmall = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

#image reformation
def image_reform(image1, width, height):
    image1 = image1.convert('RGB')
    image1 = image1.resize((240, 135), Image.BICUBIC)
    return image1
    
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Read the button value
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

status = 0
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    if not buttonB.value: # press B
        status = 0

    if status == 0 and buttonA.value and buttonB.value: 
	# without any button pressed
        # Display percentage of the day
        hr = time.strftime("%H")
        mo = time.strftime("%M")
        sec = time.strftime("%S")
        now = int(hr) * 60 * 60 + int(mo) * 60 + int(sec)
        percentage = round(now / 86400 * 100, 3)
        textDisp = str(percentage) + "% of the Day"
        showWidth = int(width * percentage / 100);
        
        # Draw the battery interface
        if percentage <= 25:
            draw.rectangle((0, 0, showWidth, height), 
            outline=0, fill="#D10000") # red
        elif percentage <= 50:
            draw.rectangle((0, 0, showWidth, height), 
            outline=0, fill="#FF8C00") # orange
        elif percentage <= 75:
            draw.rectangle((0, 0, showWidth, height), 
            outline=0, fill="#FFC300") # yellow
        else:
            draw.rectangle((0, 0, showWidth, height), 
            outline=0, fill="#00D100") # green
    
        draw.text((10, height/2.5), textDisp, font=font, fill="#FFFFFF")
    
        # Calculate the hours left
        timeLeft = str(24 - int(hr) - 1) + " hrs " + str(60 - int(mo) - 1) + " mins to Go"
        draw.text((width * 0.25, height * 0.75), timeLeft, font=fontSmall, fill="#FFFFFF")
        # Display Guideline for the buttoms  
        draw.text((0, 20), "<- find ways to kill time", font=fontSmall, fill="#FFFFFF")
	# Display image
        disp.image(image, rotation)
        time.sleep(1)


    if buttonB.value and not buttonA.value:  # press button A
        fileName = ["netflix.PNG","videogame.jpeg","tiktok.WEBP",
		"shopping.jpeg","spotify.jpeg","workout.jpg", 
		"book.jpeg","bakery.jpeg", "boardgame.jpeg"]
        image1 = Image.open(random.choice(fileName))
        image1 = image_reform(image1, width, height)
        draw = ImageDraw.Draw(image1)
        draw.text((0, 20), "<- Roll the Dice", font=fontSmall, fill="#FFFFFF")
        draw.text((0, 100), "<- clock", font=fontSmall, fill="#FFFFFF")
        disp.image(image1, rotation)
        status = 1

	


