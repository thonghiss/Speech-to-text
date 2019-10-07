from gtts import gTTS
import time, os

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'audio.mp3'
    file.save(filename)

    os.system('audio.mp3')