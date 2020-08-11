from gtts import gTTS
import os


def cupcakeResponse(audio):
    my_obj = gTTS(text=audio, lang='en', slow=False)
    my_obj.save("response.mp3")
    print(f"Cupcake: {audio}")
    os.system("mpg321 -q response.mp3")
