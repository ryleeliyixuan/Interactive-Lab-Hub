# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm. [Ruoyu Zhou] \*\*\***
* __Contours__
  * __Design - Replacement of Background__: It’s easy for a contours algorithm to detect object borders and localize objects in an image. We can use it to replace the background of an image with another, all we need is to perform image-foreground extraction (similar to image segmentation). Contours is an approach that can be used to perform such segmentation.
  * __ScreenShot__: 

![a-opencv-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-opencv-1.png)

* __Face-detection__
  * __Design - Hair Line Calculator__: The face-detection algorithm can detect inner features(mouth, nose, eyes) and also outer features(head shape, hairlines). We can use it as a Hair Line Calculator, which can be used to calculate the estimated time it will take to be bald based on the position movement of people’s hairline.
  * __ScreenShot__: 

![a-opencv-2](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-opencv-2.png)

* __Optical-flow__
  * __Design - Toy car racing tracker__: The optical-flow detects the motion of objects or the webcams. We can use it to build a toy car racing tracker. If the toy car runs out of the original line it loses the game. We can see from the picture when it gets across the middle line.
  * __ScreenShot__: 

![a-opencv-3](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-opencv-3.png)

* __Object-detection__
  * __Design - Room copy app__: The object-detection algorithm can locate objects. We can use it to build a room copy app. When someone finds that the furniture and decorations in a vlog are attractive and they want to copy those decorations, they can use what we have designed to copy the room and get a list of items and their positions.
  * __ScreenShot__: 

![a-opencv-4](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-opencv-4.png)
#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.[Jingchun Huang]\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

* __Gesture Recognition__
  * __About this Tool__: MediaPipe is used to detect the percentage of the pinching of hands. In the screen of this script, it shows the skeleton of hands and the percentage of how much the hand is pinched. So when you open the palm, it will reach 0%, vice versa. 
  * __Video of Playing with this Tool__: [here](https://youtu.be/Jp6AUvShyy0)
  * __Design - Pinch Instruction for Climbing__: In climbing, pinch is quite an important skill for climbers to hold those shallow hand points. Fingers are used and it can be tiring. When you take a high-level climbing track, like 5.11 or above, this skill can be used very frequently. So we can create a pinching instruction box for climbers. It can tell them how well they use this skill. Also, there can be a pattern for the pinch percentage and the difficulty level of the climbing track. For instance, level 5.11 needs 65% pinch, and level 5.6 only needs 30% pinch.



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options. [Yixuan Rylee Li]\*\*\***
*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*

* __Whether we make our own model or not:__ We made our own model to detect whether the user is wearing a mask or not. 
* __How we might use this to create your own classifier:__ We use Teachable Machines to create a classifier that could classify frames to the following three classes: 1) With Mask Class: users with a face mask on 2) Without Mask Class: users without a face mask on 3) Background Class: have nothing in view. 
* __Video of the Implementation can be found here:__ [here](https://youtu.be/pIRBphQYEcQ)
* __Screenshots can be found here__: 
  * Without Mask Class: ![a-tm-1](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-tm-1.png)
  * With Mask Class:
![a-tm-2](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-tm-2.png)
![a-tm-3](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-tm-3.png)
  * Background class:
![a-tm-4](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/a-tm-4.png)

* __Tensorflow file of this model can be found here:__ [here](https://drive.google.com/drive/folders/1_L4p6qSrlTtcsG7IY8zK2dcVkNk3blhh?usp=sharing)
* __Include what different affordances this method brings, compared to the OpenCV or MediaPipe options:__
Compared to the OpenCV or MediaPipe options, Teachable Machines allow us to train our own device to create machine learning models and recognize our own images, sounds, & poses. We can gather and group our examples into classes that we want the computer to learn. And Teachable Machine is very flexible since we can capture examples live. We can even export our model for different projects (ie. sites, apps, and etc). 



### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

We came up with 2 ideas, pitch them to potential users, and chose the second one (ie. Squid Game Candy Chanllenge).
* __Ruoyu’s idea for Teachable Machine:__
  *  __Interaction:__ Measuring the connection between art visitors and pieces of art or relics in a museum is the core step. The goal is to quantify the time a user spends looking at a piece of art or relics, and compare to extract potential patterns. We can simplify the problem by calculating the time each user spends looking at different pieces of art. 
  *  __Method:__ We should find individual patterns and identify what type of art or cultural relics the user is more engaged with. Ideally, this could be done by measuring the eye gaze or even biometrics data, such as heart rate or skin conductivity. A good environment for it is a controllable environment taking into account the limitations of the Pi camera(privacy issues).
  *  __Algorithm:__ The algorithm can classify 3 classes: (1) Looking at Left(it can be an ancient Egyptian clay bowl), (2) Looking at Right(it can be an ancient China painting), or (3) Looking at nothing. In the cases where the class is none of them, the algorithm still needs to make the most probable guess.
  * __Problem:__ But the problem is if we put it into an exhibition, the model should be trained for every different face.

* __Yixuan Rylee Li’s idea for Teachable Machine(Chosen one)__
  * __Idea:__ Squid Game Dalgona Candy Challenge
![b-dalgona-candy-game-social](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/b-dalgona-candy-game-social.jpeg)
  * __Background:__ The challenge sees players trying to carve a design or shape – such as a circle, triangle or umbrella into a piece of honeycomb candy known as dalgona, a popular Korean street food treat. Winners get to progress onto the next challenge in a series of childhood games. However, anyone who cracks the candy, even slightly, gets shot dead by the soldiers.
  * __Interaction:__ We use the teachable machine developed by Google to identify if the candy is cracked or not. We’ll place the detector (ie. camera) over the participants. When the race starts, our observant system will keep track of the shape of the candy to detect if the candy is cracked or not. If the candy is cracked or the time runs out and the participants haven’t carved out the dalgona, our Raspberry Pi will sound alert that they are eliminated from the game. And winners will be notified that they can proceed to the next round. 
![b-interaction](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/b-interaction.jpg)




### Part C
### Test the interaction prototype

* __Prototype Version 1:__ 
  * We only trained one shape (ie. circle) of candy for this version. We will later iterate our prototype based on the flight test we implement with potential users. [Video of the tensorflow model can be found here.](https://youtu.be/3UqkNbG3vNg)
  * Our Model: ![c-classification](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/c-classification.png)
* __Possible iteration and refinement:__ 
  * 1. We can train our model for multiple shapes (ie. triangle, circle, star, and umbrella).
  * 2. We can have a count down on the Raspberry Pi. 
  * 3. We can voice alert to notify the result of the game. 
  * 4. We can identify the face of the participants to rule out the loser from our system.
  * 5. … 


Now flight test your interactive prototype and **note down your observations**:
We flight test our prototype on Raspberry Pi and had following observations:
* __Goal:__ 
  * The system is supposed to detect if the candy is cracked or not.
* __Failure / Scenarios / Reasons Behind:__
  * The system works smoothly when the candies are placed on a table with simple color and shape. But when we switch to the background with messy shapes and colors it fails a lot. 
  * Stability is also a crucial factor that decides whether the system can detect the candy status. When the camera is not stabilized, it takes longer to detect the objects and would fail to do so sometimes. With multiple tests, we found that using the camera from different angles and heights led to different results. 
  * Also, the lighting in the room can influence if the system can successfully report the result. 
  * Another reason for failure is that the object border is not clear enough. Besides the shapes of the candy itself, the contrast between the candy and the surrounding would affect whether it can be detected correctly. 

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
* __Are they aware of the uncertainties in the system?__
  * Users might not be fully aware of the uncertainties in the system unless specifically marked. Users will not be able to test the angle and height of the camera, they also will not pay much attention to the background and the room lights when playing this game. 
* __How bad would they be impacted by a miss classification?__
  * From the original game setting, those who lose the game will be shot. If there are a huge number of misclassifications, many innocent users will be killed. 
  * Back to our own setting(we won’t kill people), users will not get to know if they are doing well or not but keep receiving the wrong message from the system. 
* __How could change your interactive system to address this?__
  * We should train our model again with more winning and bad examples. 
* __Are there optimizations you can try to do on your sense-making algorithm.__
  * One concern is to differentiate between candy on the table and the table itself. If the system regards the table as a big candy placed onto the table, even if it is not cracked, the first time the user uses the scissor to cut off the shape the system will regard it as a failure. 


### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***
* __What can you use X for?__
  * We can use the observant system to detect cracked shapes. It can be used in this game from our initial setting. On a larger scale, it can also be used to detect if the floor is messy, if the shirt is dirty and if the painting is in the right place of the wall, all of them can be treated as a kind of cracked shape if we capture the out of range tracks or shapes. 
  * [This system detects a circular candy that has been successfully carved out (Win). Video can be found here.](https://youtu.be/tpUeLUucN_o)
  * [This system detects a circular candy that has been cracked (Fail). Video can be found here.](https://youtu.be/B9SR9n2ZWls)
* __What is a good environment for X?__
  * A good environment would have good lighting which can present each candy clearly in the camera, and there should be enough contrast between each candy as well as the background.
  * 
* __What is a bad environment for X?__
  * A bad environment might be places without much lighting. This might cause the system to fail in detecting certain shapes from the background. Other factors like the colors and sizes of the candy can also influence the result. If the candy is too small with a broad background, the system will fail with no doubt. Places, where the colors are similar to the candies, are also a bad environment. 
  * [If we place the camera too close to the candy, it's also considered as a bad environment. Video can be found here.](https://youtu.be/B-92lXdEl_U)
* __When will X break? When it breaks how will X break?__
  * It will break when there is too much motion of the camera because the delay is quite bad. The low accuracy of the model will lead to the failure of the system.
* __What are other properties/behaviors of X? How does X feel?__
  * The system will display the result on the screen. If the user wins the game, it will say that you win this round with the same words on the screen. If the user fails, it will read out the warning to remind the user of losing the game. 


### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.
**\*\*\*Include a short video demonstrating the finished result.\*\*\***

#### Prototype - Iteration 2
* __Train our model for two shapes of two states:__ Our system is to determine whether the candy is cracked or not. Circles and triangles are the chosen shapes, and they have the states of cracked(F), not cracked(T). So there are four labels in our model. 
  * [This system detects a triangular candy that has been successfully carved out (Win). Video can be found here.](https://youtu.be/jubUEWHmhjU)
* __Further train our model for different environment:__ From the pilot test we ran with potential users in part 1, we figured out that we should further improve our model. And we made improvements in following aspects to avoid errors in different environments:
  * Add a background class
  * Add more class: During our recent tests, we found 2 states (ie. cracked(F) and not cracked(T)) were not enough for our scenario. We further extended them into 3 states (ie. cracked(F), carved out(T), and still working on the candy(W)). Further explanations can be found in the following pic:

![2-states](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/2-states.jpg)
  * Train the model with 200+ images: so the model can works for more settings/environments (ie. lighting, distance between the candy and the device, background color).
  * Consider the case that the participant's hands cover the candy: from our pilot test, we found that the participant tended to cover some portion of the candy with his hands while working on the candy. We don't want to misclassify this instance as fail. We add more image samples on this case to avoid misclassification.  
* __Add both voice, words, and lighting feedback:__ Based on the feedback we received last week, we wish to improve our system by adding both voice, words, and lighting feedback. All of these feedbacks are designed to enhance convenience and promote user accessibility. 
  * When the system detects a crack on the candy, there will be a ‘You Fail’ message displayed on the screen with the same voice message coming out. A red light will flash in this case to represent a strong warning of failure. 
  * In another case, if the user wins the game, the system will say “You win this round” with the same message displayed on the screen. With these add-on functions, the users will not need to stare at a screen to figure out if they are doing well. Users with disabilities can also use the system easily with the assistance of voice.



#### Prototype - Iteration 3
We thought about a few possible designs and implemented these designs.
* Possible Designs: ![2-design](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%205/2-design.jpg)

We realized that the stability of our camera matters a lot in our scenario. So we went with the first design as it fixed the distance bewteen the candy and the camera. 

