# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

* __Pet Camera__
  * __Real-time alerts + Info Display:__ Get notified of any activity at home with instant sound and motion alerts. Alert the pet owners about the temperature and moisture levels of the environment. 
  * __Smooth 2-way audio:__ Speak to pets and hear them bark or meow back. 
  * __Body temperature tracker:__ The camera detects the pets and follows them using machine learning algorithms. The sensor will detect their body temperature and notify the pet owners if there’s a health issue. 
  * __Check if the pets have drunk water:__ We will place the water fountain under the device. We will count every time when the pets drink water and alert the owner whether the animals drink enough water that day.  

![a-design-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/a-design-2.jpg)

* __Remote Garage Door Opener__
  * The doorman can remotely control the garage door without actually presenting there.  
  * The sender will detect the license plate and send back the plate number to the doorman who works in the lobby.
  * The reader receives the plate number and displays it on the OLED screen. Once the doorman checks the plate number, he presses the button to open the garage door. 

![a-design-2](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/a-design-1.jpg)

* __Walkie Talkie__
  * Connecting with your close friends with the design based on the message system. You can type a message or just talk to your friends directly. Also, more people can join as they form a group chat. 
* __Emergency Contact with Doctors__
  * The message system is for the communication between inpatients or patients staying in their home for further recovery and their doctors. If there is an emergency, the patient is capable of talking to their doctors and asking for help immediately. 
* __Simple Communication in Construction site__
  * Sometimes simple communication is needed in the construction site. For instance, if a bridge is under construction and only cars in a single way are allowed to pass through the bridge, the worker on one side of the bridge can use the prototype to contact their colleagues. Then the car in another way can be allowed to pass and a switch is done.





### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

The touched interface is shown in the explorer. A screenshot can be found here: 

![c-mqtt](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/c-mqtt.png)

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

We added one button and implemented the data streaming with it. [A short video illustrateing how we implement the data streaming with it can be found here.](https://youtu.be/Y864tUGtfNU) We read the status of the button and encode it into "inquiry sent" once pressed. 

![add-button](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/c-add-button.jpeg)


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

* Change the variable “topic” in line 58 for allowing any other user to publish their own color. The variable stands for an address, so if the user name is added after it, like ‘IDD/colors/panda’. Then this user is able to publish his color to the channel. Modified code is in [color_modified.py](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/color_modified.py).

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

* We are designing __a senior care daily check device.__ Many elderlies live alone and haven’t received much attention from others, especially during the pandemic. There are a number of cases where old people die out of sudden illness but no one discovers until the corpse smell is prevalent on the floor. Our system is aiming at eliminating such cases by enabling remote family members to keep an eye on the elderly through a single button for daily check-in. We nudged the check-in by reporting the local weather and didn’t use cameras to capture movements for security and privacy concerns.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?
![flow](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/c-flow.jpg)
![system-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/c-system-1.jpg)
![system-2](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/c-system-2.jpg)

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

* This is the prototype we built. The right one is the sender and the left one is the reader.
* We do think about the user interface by display instruction on the screen. Details can be found in the video.
* Codes can be accessed [here](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/tree/Fall2021/Lab%206/senior-daily-care-checkin)

![prototype](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%206/e-prototype.jpeg)

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

* [A final video of implementation can be found here.](https://youtu.be/c2siOMHmmY4)



