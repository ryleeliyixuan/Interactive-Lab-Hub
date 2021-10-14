#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import json
import sys
import os
import wave

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), "a b c d e f g h i j k l m n o p q r s t u v w x y z one two three four five six seven eight nine oh [unk]")

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        audio = json.loads(rec.Result())
        print ("\nPlease verify the following content:", audio['text'], "\n")