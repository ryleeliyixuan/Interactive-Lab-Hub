import subprocess
import time
import qwiic_button
from PIL import Image, ImageDraw, ImageFont
import digitalio
import board
import adafruit_rgb_display.st7789 as st7789

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

def handle_speak_record(content, path):
    subprocess.run(["sh", "GoogleTTS_demo.sh", content, path])
    time.sleep(1)

def handle_speak(val):
    subprocess.run(["sh", "speak.sh", val])
    time.sleep(1)

def play_sound(val):
    subprocess.run(["sh", "playsound.sh", val])
    time.sleep(1)

def take_photo():
    subprocess.run(["sh", "takePhoto.sh"])
    time.sleep(1)

redButton = qwiic_button.QwiicButton(address=0x6f)
redButton.begin()
redButton.LED_off()

if not redButton.begin():
    print("\nThe Red Qwiic Button isn't connected to the system. Please check your connection")

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
fontSmall = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

draw.text((0, 0), "STEP1: \n RECORD \n YOUR \n INFORMATION", font=font, fill="#FFFFFF")
disp.image(image, rotation)
handle_speak_record("Welcome to Cornell Tech Surveillance Testing! What's your first name? Please spell it out.", "firstname.wav")
handle_speak("First name verified. Your first name is: ")  
play_sound("firstname.wav")

handle_speak_record("What's your last name? Please spell it out.", "lastname.wav")
handle_speak("Last name verified. Your last name is:")  
play_sound("lastname.wav")

handle_speak_record("What's your net ID? Please spell it out.", "netid.wav")
handle_speak("Net ID verified. Your net ID is:")  
play_sound("netid.wav")

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((0, 0), "STEP2: \n SCAN \n BARCODE", font=font, fill="#FFFFFF")
disp.image(image, rotation)
handle_speak("Please pick up one testing kit on your right side.")
time.sleep(3)
handle_speak("Please use the camera in front of you to take a picture of your barcode on the test tube. When you are ready, please press the red button.")

while True:
    if redButton.is_button_pressed():
        redButton.LED_on(155)
        handle_speak("TAKE PHOTO NOW!!!")
        take_photo()
        handle_speak("Your unique barcode has been successfully recorded.")
        redButton.LED_off()
        break

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((0, 0), "STEP3: \n COVID \n TESTING", font=font, fill="#FFFFFF")
disp.image(image, rotation)
handle_speak("Now, follow the guidance displayed on the screen. If you need assistance, please press the red button, staff will come to you shortly.")
handle_speak("If you finished testing, place the tube in the bucket on your left side. Thanks for caring the Cornell Tech community by participating the weekly surveillance testing.")

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "1. Remove the swab from \n the wrapping \n 2.Put the soft tip into \n your right nostril \n 3. Rotate the wap in \n a circular pattern 5 times \n 4. Repeat the swabbing steps \n in your left nostril", font=fontSmall, fill="#FFFFFF")
    disp.image(image, rotation)
    if redButton.is_button_pressed():
        redButton.LED_on(155)
        handle_speak("A staff will come to you shortly. Please wait patiently. If our staff haven't reached you in 2 mins, please press the button againcc.")
        redButton.LED_off()

