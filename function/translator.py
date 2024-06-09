import os
import sys
sys.path.insert(0, os.path.abspath('./function/'))
# print(sys.path)
import time
import vlc
import speech_recognition  as sr
import googletrans
from gtts import gTTS
from auxiliary.utils import play_audio, recognize_audio
from pygame import mixer
mixer.init()

# Listen and Translate
def listenTo(fromLanguage, toLanguage):
    r = sr.Recognizer()
    translator = googletrans.Translator()
    with sr.Microphone() as source:
        print("Express what you want to translate...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        stt_text = r.recognize_google(audio, language=fromLanguage)
        print(f'You say: {stt_text}')
        translated_text = translator.translate(stt_text, dest=toLanguage).text
        print(f'After translating: {translated_text}')
    return translated_text

# Text-to-Speech
def speak(sentence, mp3_name):
    tts = gTTS(text=sentence, lang='zh-tw')
    tts.save(mp3_name)
    # mixer.music.load('{}.mp3'.format(mp3_name))
    # mixer.music.play()

# Set languages type
def set_language(rec_text):
    language = {'TW':"zh-TW", 'USA':"en", 'French': 'french', 'GER': 'german', 'Japan': 'japanese','Netherlands': 'dutch'}
    if rec_text == '中文翻英文':
        fromLanguage = language['TW']
        toLanguage = language['USA']
        play_audio('./audio/TW_to_En.mp3')

    elif rec_text == '英文翻中文':
        fromLanguage = language['USA']
        toLanguage = language['TW']
        play_audio('./audio/USA_to_TW.mp3')

    elif rec_text == '中文翻日文':
        fromLanguage = language['TW']
        toLanguage = language['Japan']
        play_audio('./audio/TW_to_Japan.mp3')

    elif rec_text == '中文翻法文':
        fromLanguage = language['TW']
        toLanguage = language['French']
        play_audio('./audio/TW_to_French.mp3')

    elif rec_text == '中文翻荷蘭語':
        fromLanguage = language['TW']
        toLanguage = language['Netherlands']
        play_audio('./audio/TW_to_Neth.mp3')

    return fromLanguage, toLanguage

# Translator
def translate(audio_path, fromLanguage, toLanguage):
    rec = sr.Recognizer() 
    listen_text=listenTo(fromLanguage, toLanguage)      # Listen and Generate translated text
    speak(listen_text, audio_path)                      # Text to Speech                
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(audio_path)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    duration=player.get_length()/1000
    time.sleep(duration)

if __name__ =='__main__':
    audio_path = '../audio/translate.mp3'
    while True:
        set_txt = recognize_audio(display_text="Say the setting of languages.....")
        fromLanguage, toLanguage = set_language(set_txt)
        translate(audio_path, fromLanguage, toLanguage)
    