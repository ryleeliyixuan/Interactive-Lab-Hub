
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import time
import subprocess
import qwiic_button
import qwiic
import digitalio
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

i2c = board.I2C()

redButton = qwiic_button.QwiicButton(address=0x6f)
redButton.begin()
redButton.LED_off()

if not redButton.begin():
    print("\nThe Red Qwiic Button isn't connected to the system. Please check your connection")

def handle_speak(val):
    subprocess.run(["sh", "speak.sh", val])
    time.sleep(1)

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())


while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print("I think its a:",labels[np.argmax(prediction)])
    label = labels[np.argmax(prediction)]
    if label == "C-F" or label == "T-F":
        print("You Failed!")
        redButton.LED_on(155)
        handle_speak("You Failed!")
	# start with a blank screen
        oled.fill(0)
        # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
        oled.show()
        # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "You Failed！", font=font, fill=255)
        # Display image
        oled.image(image)
        oled.show()
    if label == "C-T" or label == "T-T":
        print("You Win!")
        redButton.LED_off()
	# start with a blank screen
        oled.fill(0)
        # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
        oled.show()
        # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "You Win!", font=font, fill=255)
        # Display image
        oled.image(image)
        oled.show()
        handle_speak("You win!")
    if label == "C-W" or label == "T-W":
        print("In Progress!")
        redButton.LED_off()
	# start with a blank screen
        oled.fill(0)
        # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
        oled.show()
        # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "In Progress!", font=font, fill=255)
        # Display image
        oled.image(image)
        oled.show()


    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
