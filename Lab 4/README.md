# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***
#### Eye-caring Clipboard
The eye-caring clipboard prevents vision impairment & blurred eyesight by alerting users with sounds if they write/read in a wrong posture that place their heads too close to the book (<30cm).
![eye-caring-clipboard-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-eye-caring-clipboard-1.jpg)
![eye-caring-clipboard-2](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-eye-caring-clipboard-2.jpg)

#### Parking Assistant
This rear parking assistant device detects the distance between the car and any obstacle behind and alert users about the distance.
![parking-assistant](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-parking.jpg)

#### Social Distance Detector
This social distance detector detects the distance between users and any human objects and alerts with sounds whenever users violate social distance rule (< 6 feet). Its camera connects to the car system so that the rear view would show up in the dashboard of the control system. 
![social-distance](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-social-distance.jpg)

#### Water-Level Logger
This water-level logger features a distance detector at the bottom of the box and an ajustable supporter that helps the device stand stably in the river. It detects the distance between itself and the water surface. The raspberry Pi would log the water level on hourly basis and send back logs to the server on the shared Wi-fi network on daily basis. 
![water-level logger](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-water-level-logger.jpg)

#### Doorbell Camera
This doorbell camera shall be attached on the door with stickers. It would start to record when moving objects enters the sight (<3m).
![doorbell-camera](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/c-doorbell-camera.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***
* How shall we position the sensor such that it's at the right angle to detect the distance we aim to extract?
  * For the "Eye-caring Clipboard" case, we need to choose the right angle to detect the distance between users' eyes and the paper on the clipboard. If we placed the sensor entirely facing the ceiling (90°), it would be hard to capture any human object and detect the distance. If we placed the sensor entirely facing the users (0°), the sensor would detect the distance between the users' bodies and the paper on the clipboard, which is not our target distance and might result in a false alert due to miscalculation. 50° to 30° would be a reasonable range but we still need to physically prototype the position of the sensor to understand the best angle.
  * For the "Parking Assistant" case, if the sensor was placed vertically, it could detect any obstacle that rise above the ground with a height greater or equal that the height of the sensor above the ground but miss those with a height above the ground less than that of the sensor. We still need to physically prototype the position of the sensor to understand the best angle. Or we can use the camerca to detect obstacles and adjust the angle dynamically. 
* How shall we design the appearance of our device such that we can fit in the Raspberry pi in a way that does affect the aesthetics of our device? 
  * In response to this, we still need to physically prototype the appearance of our device.

**\*\*\*Pick one of these designs to prototype.\*\*\***

I picked the "Eye-caring Clipboard" to prototype. 

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

This device needs to integrate a text display and a distance sensor. The main focus of our design is the position of the display and sensor. Following is the list of designs I am considering.  
![physical-display](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/d-physical-display.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***
* Do we need to crop a hole on the clipboard to fit in the sensor and display? We need to physically prototype the placement of the display and the sensor to understand this.
* How to make the angle/direction of the sensor adjustable? Do we need a handle/knob to control the angel of the distance sensor? (Is it possible to realize the calculation for different angles using some sort of algorithm so that we don't have to adjust the angle to a fixed value?)
* What would be the depth of the clipboard in order to fit the Raspberry pi underneath it? We need to measure the depth of the Raspberry Pi to figure out the problem. 
* Would the placement of sensor affect users' writing/reading experience? Need to find the right position of the sensor on the clipboard such that if users place paper/notepad on it, paper/notepad would not cover the sensor.


**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I decided to go with design no.5. 

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)
* In order to fit in the text display and the distance sensor, the size of clipboard (230mm x 295mm) is a litte bit larger than letter-size (215.9mm x 279.4mm).
* I hide the Raspberry pi beneath the board such that it does not affect the aesthetics of our device.
* I choose to place the display and sensor on the very top of the clipboard such that paper/notepad would not cover them. Also in this way, users can track the distance with the text display while writing/reading.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

* Front: this left corner is the distance sensor and the right corner is the text display. 
![d-cardboard-front](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/d-cardboard-front.jpeg)

* Back: 
![d-cardboard-back](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/d-cardboard-back.jpeg)

* Video of My Cardboard Prototype: 
*[Video of My Cardboard Prototype](https://youtu.be/jt__6ufoJOM )*

LAB PART 2

## Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part F
### Feedback: 
Yixuan! I thought the posture correction idea is great. Interesting too to see how you wanted to connect it to a clipboard. I was thinking though, it would be useful for someone like me too who always sits in front of her computer. I think it would be interesting to design the posture corrector as a clip that you can attach to anything you are looking at. Or even as a necklace, with the sensor aligned upright facing the back of your neck. That way if the distance exceeds x, that means the person is slouching. Overall think the idea is interesting but the form factor I think has so much potential! - Angelica Kosasih

### Iteration 1: 
Thanks for Angelica's feedback! I decided to take her advice. I destilled the idea of "eye-caring clipboard" to make the device working for multiple scenarios. Not only for writing & reading with clipboard, also for all kinds of working environments (laptops, tablets, paper and etc). I thought about three possible designs, two of which are wearables: 
![f-gesture-corrector](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/f-gesture-corrector.jpg)
I picked the non-wearable design because of the following reasons:
* The necklace may be too heavy for users as we need to integrate our Raspberry Pi into the device.
* The watch moves along with hand movement (writing, typing and clicking). We are aiming to detect the distance from the head to the interface. If we implements the device in form of watch, the distance detected is not our target distance. 
* The stand-alone idea is the best option as we can place the device wherever we want. We can detect the target distance as long as we make the distance sensor facing direct to the user's head.

This is the design for iteration 1:
![f-iteration-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%204/f-iteration-1.jpg)
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

