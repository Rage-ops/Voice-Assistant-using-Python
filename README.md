# Voice-Assistant-using-Python

## Capabilities
* Detects number of Faces from an image.
* Opens any website in the browser.
* Communicates with Datamuse API for word finding queries.
* Launches any system application .
* Plays Tic Tac Toe, flips a coin and rolls a die randomly.
* Tells you info for anything you ask from wikipedia.
* Tells you the current date and time.

## Modules Used:
* import speech_recognition as sr
* from random import randint
* import datetime
* from gtts import gTTS
* from sys import exit
* import re
* import os
* import wikipedia
* import webbrowser
* import requests
* import json
* import cv2

## Functions

### speech.py
* def my_command(): # Speech to text using speech_recognition module
* def help_me(): # Tells what assistant can do.
* def pattern_search(pattern, string): # matches a pattern from the text using regex

### response.py
* def cupcakeResponse(audio): # Text to speech using gtts library.

### datamuse.py
The Datamuse API is a word-finding query engine for developers. You can use it in your apps to find words that match a given set of constraints and that are likely in a given context. You can specify a wide variety of constraints on meaning, spelling, sound, and vocabulary in your queries, in any combination.

* def data_muse_request(param):  # returns up to first four words from the result of the request made to data muse api
* def mean_like(word):  # returns words with a meaning similar to the given word
* def sound_like(word):  # returns words that sound like the given word
* def spelled_like(word):  # words that are spelled similarly to the given word
* def rhyme_like(word):  # returns words that rhyme with the given word
* def adjective(word):  # returns adjectives that are often used to describe given word

### facerec.py
* def face_recognise(path): # returns number of faces detected in the image using OpenCV

### openapps.py
* def open_app(app_name): # launches the application
