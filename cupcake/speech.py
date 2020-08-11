import speech_recognition as sr
from random import randint
import datetime
from sys import exit
import re
import wikipedia
import webbrowser

from openapps import open_app
from facerec import face_recognise
from response import cupcakeResponse
import datamuse


def pattern_search(pattern, string):
    matches_ = re.search(pattern, string)
    if matches_:
        return re.search(pattern, string).groups()


def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nSay something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio_said = r.listen(source)
    try:
        command = r.recognize_google(audio_said).lower()
        print('\nYou said : ' + command + '\n')
    except sr.UnknownValueError:
        print('....\n')
        cupcakeResponse("Sorry, I don't understand.")
        command = my_command()
    return command


def help_me():
    cupcakeResponse(f"Hey there {USER}! I'm Cupcake, your voice assistant. There's a lot I can help with.\n")
    commands = ["Detect number of Faces", "Tell about Google", "Synonym of beautiful", "Words that sound like bat",
                "Words that spell like cup", "Launch Firefox", "Words that rhyme with love", "Open youtube.com",
                "Tic Tac Toe", "Flip a Coin", "Roll a die", "Date and Time"]
    cupcakeResponse('Try saying:')
    for command in commands:
        print(command)
        cupcakeResponse(command)


cupcakeResponse('Say your Name')
USER = my_command()
help_me()
audio = my_command()
while True:

    if 'help me' in audio:
        help_me()

    # Greet
    if 'hey cupcake' in audio:
        text = f"Hey {USER}. That's me. How can I help you?️"
        cupcakeResponse(text)
        audio = my_command()

    elif 'hey' in audio or 'hi' in audio:
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            cupcakeResponse(f'Hello {USER}. Good morning')
        elif 12 <= current_hour < 18:
            cupcakeResponse(f'Hello {USER}. Good afternoon')
        else:
            cupcakeResponse(f'Hello {USER}. Good evening')

    # Time
    elif 'time' in audio or 'date' in audio:
        current_time = datetime.datetime.now()
        cupcakeResponse(f"Today's date is {current_time.date().strftime('%d-%m-%Y')} and"
                        f" current time is {current_time.hour} hours {current_time.minute} minutes")

    # Face Recognition
    elif 'detect number of faces' in audio.lower():
        path = input("Enter the Image Path:")
        cupcakeResponse('detecting...\n')
        face_recognise(path)

    # Launching app
    elif 'launch' in audio:
        app_name = pattern_search(r"launch (.+)", audio)
        if app_name:
            open_app(app_name[0])
        else:
            cupcakeResponse('Sorry the requested task could not be completed')

    elif 'tic tac toe' in audio:
        cupcakeResponse('Opening TicTacToe game')
        webbrowser.open('https://trinket.io/pygame/712948d483')

    # Opening in Browser
    elif 'open' in audio:
        website = pattern_search(r"open (.+)", audio)
        if website:
            domain = website[0]
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            cupcakeResponse(f'The website {url} has been opened.')
        else:
            cupcakeResponse('Sorry the requested task could not be completed')

    elif "flip a coin" in audio:
        r1 = randint(0, 1)
        cupcakeResponse("It's HEADS\n") if r1 == 0 else cupcakeResponse("It's TAILS\n")

    elif "roll a die" in audio:
        r1 = randint(1, 6)
        cupcakeResponse(f"You got {r1}\n")

    # Datamuse - word finding queries
    elif "synonym of" in audio:
        matches = pattern_search(r"synonym of (.+)", audio)
        if matches:
            res = datamuse.mean_like(matches[0])
            if len(res) == 0:
                cupcakeResponse('Sorry, Nothing Found!')
            else:
                print(res)
                for word in res:
                    cupcakeResponse(word)

    elif "sound like" in audio:
        matches = pattern_search(r"words that sound like (.+)", audio)
        if matches:
            res = datamuse.sound_like(matches[0])
            if len(res) == 0:
                cupcakeResponse('Sorry, Nothing Found!')
            else:
                print(res)
                for word in res:
                    cupcakeResponse(word)

    elif "spell like" in audio:
        matches = pattern_search(r"words that spell like (.+)", audio)
        if matches:
            res = datamuse.sound_like(matches[0])
            if len(res) == 0:
                cupcakeResponse('Sorry, Nothing Found!')
            else:
                print(res)
                for word in res:
                    cupcakeResponse(word)

    elif "rhyme with" in audio:
        matches = pattern_search(r"words that rhyme with (.+)", audio)
        if matches:
            res = datamuse.rhyme_like(matches[0])
            if len(res) == 0:
                cupcakeResponse('Sorry, Nothing Found!')
            else:
                print(res)
                for word in res:
                    cupcakeResponse(word)

    elif "adjectives to describe" in audio:
        matches = pattern_search(r"adjectives to describe (.+)", audio)
        if matches:
            res = datamuse.adjective(matches[0])
            if len(res) == 0:
                cupcakeResponse('Sorry, Nothing Found!')
            else:
                print(res)
                for word in res:
                    cupcakeResponse(word)

    # ask me anything
    elif 'tell me about' in audio:
        matches = pattern_search('tell me about (.+)', audio)
        try:
            if matches:
                topic = matches[0]
                page = wikipedia.page(topic)
                cupcakeResponse(page.content[:300])
                cupcakeResponse(f'Know more at {page.url}')
        except Exception as e:
            cupcakeResponse(e)

    elif 'quit' in audio:
        cupcakeResponse('closing now!\n')
        exit(0)

    else:
        cupcakeResponse("Sorry, I don't understand.")
    audio = my_command()
