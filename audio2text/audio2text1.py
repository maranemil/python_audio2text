#!/usr/bin/env python3

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

filename = "audio_chunks/out000.wav"
fh = open("recognized.txt", "w+")
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    try:
        text = r.recognize_google(audio_data, language="en-US")
        fh.write(text + ". ")
        # print(text)

    # catch any errors.
    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results. check your internet connection")
        # https://github.com/Uberi/speech_recognition/issues/132
        # https://cloud.google.com/speech-to-text/quotas

"""
https://cloud.google.com/speech-to-text/quotas


Content Limit 	Audio Length
Synchronous Requests 	~1 Minute
Asynchronous Requests 	~480 Minutes*
Streaming Requests 	~5 Minutes**


Speech Adaptation Limit 	Value
Phrases per request 	5000
Total characters per request 	100,000
Characters per phrase 	100


Type of Limit 	Usage Limit
Requests per 60 seconds* 	900
Processing per day 	480 hours of audio
"""        