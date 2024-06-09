import os
import sys
# print(sys.path)
import argparse
import time
import vlc
import speech_recognition as sr
from function.auxiliary import utils
from function import temp_control, translator, led

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mp3_path', help='Path of saving translated audio', type=str, default='./audio/translate.mp3')
    args = parser.parse_args()
   
    translated_path = args.mp3_path      # Path for saving translator file
    
    #################### Running ####################
    utils.play_audio('./audio/start.mp3')
    while(True):
        utils.play_audio('./audio/service.mp3')
        rec_txt = utils.recognize_audio(display_text="Say somethings...")
        utils.play_audio('./audio/got_it.mp3')
        if rec_txt == '開燈':
            led.led_switch()
        elif rec_txt == '測溫度':
            temp_control.run()
        elif rec_txt == '翻譯':
            utils.play_audio('./audio/language_type.mp3')
            set_request_txt = utils.recognize_audio(display_text="Say the setting of languages.....")
            fromLanguage, toLanguage = translator.set_language(set_request_txt)
            translator.translate(translated_path, fromLanguage, toLanguage)
        # # 要改停止條件
        # elif rec_txt == '檢查心跳':
        #     heart.cal_heart()
        
        else:
            break
    utils.play_audio('./audio/close_sys.mp3')
    print("========================= Shut down the system ==========================")
    
if __name__ =='__main__':
    main()