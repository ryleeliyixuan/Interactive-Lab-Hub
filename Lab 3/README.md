# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

[echoName.sh](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/echoName.sh)

[Video link of this demo can be found here](https://youtu.be/Cml-azmZnVg)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

[askZipCode.sh](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/speech2text/askZipCode.sh)

[zipcode.py](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/speech2text/zipcode.py)

![AskForZipCode_Demo_Output](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/speech2text/askForZipCode_Output.png)

[Video link of this demo can be found here](https://youtu.be/jK1FOsGXc3k)

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

For this lab, I aim to develop a Cornell Tech Surveillance Test Chatbot. I found some works are repetitive. This machine would lead to less interaction between students and staff on the testing sites by facilitating the process of pre-testing inquiry (ie. recording basic information and delivering testing tube). If students need assistance from staff, they could also seek assistance from them by pressing the button on the machine. 

![storyboard](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-storyboard.jpg)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

| Stage  | Situation     | Dialogue from the Machine                                                                                                                                              | Expected Answer from Users |
|--------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Pre    | Basic Inquiry | Welcome to Cornell Tech Surveillance Testing! What's your first name?                                                                                                  | First Name                 |
| Pre    | Basic Inquiry | Hello, what's your last name?                                                                                                                                          | Last Name                  |
| Pre    | Basic Inquiry | Is your netID xxxx? Please answer with yes or no.                                                                                                                      | Yes or No                  |
| During | Guide         | This is your testing kit. Please record the unique barcode on the testing tube for future test result access.                                                          | N/A                        |
| During | Guide         | If you need assistance, please press the red button, staff will come to you shortly. If you finished testing, place the tube in the bucket and press the green button. | Press red or green button  |
| After  | Guide         | Thanks for caring the Cornell Tech community by participating the weekly surveillance testing. You can leave now.                                                      | N/A                        |

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

[Interactive Device Design - Lab 3 Part 1 - Acting out the dialogue](https://youtu.be/47sEtJ1ga1g)

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

The dialogue seemed different than what I imagined when it was acted out in the following ways: 
* The machine is expecting a input of first/last name such as "WU". But users tend to spell out their names (eg. "W-U" instead of "WU").
* Users may answer their preffered name (eg. "Cathy") instead of their legal names that are recorded in the Cornell Tech system (eg. "Kaixi).

In response to the above feedbacks, I will revise the questions. 

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

### Feedback:
* I love how the device is focused on a very well-constrained problem that involves going through a specific series of steps. I feel like it's very easy to understand what the goal is and what success means for the device. I wish the device could do something that speeds up the instruction and exchange. For example, if the user could just speak and have the device parse their information, or (for pt2 of the lab) if the device can scan bar codes.
* This is so based on our life and interesting, the storyboard, and video demo are easy to understand. The part where the device gives the testing tube might be hard to implement. 
* Two buttons would be too much. Think of the functinality of your buttons. 

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
* My original plan is to prep the testing tube with designated barcode based on net id beforehand, read users' net id, deliver the testing tude with the pre-assigned barcode. Since the part where the device gives the testing tube might be hard to implement, it would be better that we place all the available testing tubes on the right side, ask users pick one, and then record the barcode on the testing tube. 
* I streamlined the process of barcode recording by allowing users to scan the barcodes using the extended camera on the Raspberry Pi. In this sense, users don't have to take out their phones and take the photos by themselves.
* I paraphrased the questions so that the expected answers could be more clear. (eg. from "what's your first time?" to "what's your first time? Please spell it out.") And I added dialogue that verifies the answers with users (eg. "first name verified. Your first name is xxxxx").
* I used just one button instead of two since users don't have to choose between multiple choices (eg. A or B). Two buttons may be redundant. 
* I changed the timing between each questions. Timing between those questions groupped into the same section was 0.5s. Timing between different sections was 1s.
* I assumed that staff may be busy and did not show up due to high concurrency of requests. Thus, I allowed users to press the button again to notify the admin till the staff show up.  

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

* I displayed the current step on the screen of the Raspberry Pi. Moreover, I used the screen to display the guidelines for PCR-testing so that first-time users can follow the steps.
* I used the LED light on the red button to state the status of barcode scanning. (ie. ON: barcode scanning in progress)

3. Make a new storyboard, diagram and/or script based on these reflections.

### Storyboard
![storyboard](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-storyboard-v2-3.jpg)
![storyboard](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-storyboard-v2-2.jpg)
![storyboard](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-storyboard-v2-1.jpg)

### Dialogue
| Stage        | Type          | Dialogue from the Machine                                                                                                                                                                                                                                                                                      | Excepted Answer from Users |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Record INFO  | Basic Inquiry | Welcome to Cornell Tech Surveillance Testing! What's your first name? Please spell it out.                                                                                                                                                                                                                     | First Name (eg. R-Y-L-E-E) |
| Record INFO  | Verification  | First name verified. Your first name is: xxx                                                                                                                                                                                                                                                                   | N/A                        |
| Record INFO  | Basic Inquiry | What's your last name? Please spell it out.                                                                                                                                                                                                                                                                    | Last Name (eg. L-I)        |
| Record INFO  | Verification  | Last name verified. Your last name is: xxx                                                                                                                                                                                                                                                                     | N/A                        |
| Record INFO  | Basic Inquiry | What's your net ID? Please spell it out.                                                                                                                                                                                                                                                                       | Net ID (eg. y-l-2-5-5-7)   |
| Record INFO  | Verification  | Net ID verified. Your net ID is: xxx                                                                                                                                                                                                                                                                           | N/A                        |
| Scan barcode | Guide         | Please pick up one testing kit on your right side.                                                                                                                                                                                                                                                             | N/A                        |
| Scan barcode | Guide         | Please use the camera in front of you to take a picture of your barcode on the test tube. When you are ready, please press the red button.                                                                                                                                                                     | Press red button           |
| Scan barcode | Verification  | TAKE PHOTO NOW!!!                                                                                                                                                                                                                                                                                              | N/A                        |
| Scan barcode | Verification  | Your unique barcode has been successfully recorded.                                                                                                                                                                                                                                                            | N/A                        |
| Testing      | Guide         | Now, follow the guidance displayed on the screen. If you need assistance, please press the red button, staff will come to you shortly. If you finished testing, place the tube in the bucket on your left side. Thanks for caring the Cornell Tech community by participating the weekly surveillance testing. | N/A or Press Red Button    |
| Testing      | Guide         | A staff will come to you shortly. Please wait patiently. If our staff haven't reached you in 2 mins, please press the button again.                                                                                                                                                                            | N/A or Press Red Button    |
## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
* All the scripts can be found [here](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/tree/Fall2021/Lab%203/covidtestbot)
* This is [the main class](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/covidtestbot/main.py) 
![Workflow](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-Flowchart.jpg)

*Include videos or screencaptures of both the system and the controller.*
### Final Video of Prototyping
[Final Video of Prototyping](https://youtu.be/rWOsRPjlX2g)

### Screencaptures
* Screen Display: 
![Screenshot](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-screen1.jpg)
![Screenshot](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-screen2.jpg)
![Screenshot](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-screen3.jpg)
![Screenshot](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-screen4.jpg)
* Sample photo of barcode scanning: 
![Screenshot](https://github.com/ryleeliyixuan/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-barcode.jpg)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
* Work well: The workflow the system performed was pretty clear and easy to follow. Since I only implemented one button, it's easy to use and users would not confuse the usage/functionality of buttons. And the workflow of scanning barcode worked so well as it features methods of using voice to interact, using button to take actions, and using camera to record info.
* Didn't work well: Some users may not fully understand the voice guidelines as some of the lines may take too long (~8s). It would be better if we repeat the voice guidlines again if there hears no response from users. Or we segment lengthy lines into a few pieces so it's easier for users to understand them. 


### What worked well about the controller and what didn't well 
* Work well: I used storyboards, flowcharts, role-playing and WoZ as my prototyping methods of choice. The storyboards and flowcharts illustrate the workflow well in a structured manner. The controller was easy to use, especially the text to speech functionality.
* Didn't work well: The speech recording functionality required users to speak directly to the USB microphone. It might be inconvenient for users to bend over and talk directly to the USB mircophone. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
* Users may not answer our questions in a way that aligned with our anticipation. We need to think of all possible reactions from users (eg. misunderstand the questions, record the wrong info, do not hear the questions well).
* The speech to text functionality could streamline the process of data recording. We can parse the video file into text strings and store strings in the databases.  


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
* The speech to text functionality could streamline the process of data recording. We can parse the video file into text strings and store them in the databases.
* We scanned the barcode. We can use computer vision to extract text/number on the barcode and store the info in our databases.
* We can even use the camera to take a photo of users' Cornell ID, so they don't have to record firstname/lastname/netid one by one. Or we can use a card reader. 

