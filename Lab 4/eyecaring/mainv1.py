import subprocess
import time
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


def handle_speak(val):
    subprocess.run(["sh", "speak.sh", val])
    time.sleep(1)


print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")


# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)



while True:
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		ToF.stop_ranging()

		distanceInches = distance / 25.4
		distanceFeet = distanceInches / 12.0
		print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))
		
		# start with a blank screen
		oled.fill(0)
		# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
		oled.show()
		# Create blank image for drawing.
		image = Image.new("1", (oled.width, oled.height))
		draw = ImageDraw.Draw(image)
		draw.text((0, 0), "Distance: " + str(round(distanceFeet,2)) + "ft", font=font2, fill=255)
		# Display image
		oled.image(image)
		oled.show()

		# warn if it's too close 
		if (distanceFeet < 1):
			oled.fill(0)
			oled.show()
			draw.text((0, 0), "TOO CLOSE!!", font=font2, fill=255)
			# handle_speak("Warning! Your eyes are too close to the interface!")
		
		time.sleep(.1) 


	except Exception as e:
		print(e)