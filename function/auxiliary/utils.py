import time
import vlc
import googletrans
import speech_recognition as sr

# Transform user's audio(text-to-audio)
def recognize_audio(display_text):
    r = sr.Recognizer()
    translate = googletrans.Translator()
    with sr.Microphone() as source:
        print(display_text)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        stt_text = r.recognize_google(audio, language="zh-TW")
        print(f'You say: {stt_text}')
    return stt_text

# Play audio file
def play_audio(file_name):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(file_name)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    duration=player.get_length()/1000
    time.sleep(duration)

