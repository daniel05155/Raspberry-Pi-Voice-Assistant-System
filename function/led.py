import os
import sys
sys.path.insert(0, os.path.abspath('./function/'))
# print(sys.path)
from gpiozero import LED
import RPi.GPIO as GPIO
from gpiozero import MCP3008
import spidev
import vlc
import googletrans
import speech_recognition as sr
import time
# from function.auxiliary.utils import play_audio, recognize_audio
# from function.auxiliary.mcp_data import ReadADC
from auxiliary.utils import play_audio, recognize_audio
from auxiliary.mcp_data import ReadADC

light_ch = 0                    # photoresistance 
gpio_num_one = 13               # GPIO
led_one = LED(gpio_num_one) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 1000)

#################### LED Control ####################
# Switch on/off
def led_switch():
    try:
        while(True):
            pwm.start(0)   # 開始 PWM 輸出
            adc_val = ReadADC(light_ch)
            print(f'light value: {adc_val}')
            if adc_val>=950:
                pwm.ChangeDutyCycle(100)
            elif adc_val>=800 and adc_val<950:
                pwm.ChangeDutyCycle(80)
            elif adc_val>=700 and adc_val<800:
                pwm.ChangeDutyCycle(60)
            elif adc_val>=600 and adc_val<700:
                pwm.ChangeDutyCycle(40) 
            elif adc_val>=500 and adc_val<600:
                pwm.ChangeDutyCycle(20)
            else:
                pwm.ChangeDutyCycle(5)
            time.sleep(1)
    except KeyboardInterrupt:
        pwm.stop()  # 停止 PWM 輸出
        print()
        print("========== Switch off LED  ==========")
    finally:
        GPIO.cleanup()

def flash_light():
    led = gpio_num_one
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    try:
        while True:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop executing!")
    finally:
        GPIO.cleanup()

#######################################################

if __name__ =='__main__':
    light_ch = 0    # Sensor channel
    req_txt = recognize_audio(display_text='Say control command...')
    resist_val = ReadADC(light_ch)
    if req_txt == '開燈':
        led_switch()
    if req_txt == '閃爍':
        flash_light()
    else:
        print("System can't recognize source.")
        
    # flash_light()
    # test_light()
# Only for testing
# def test_light():
#     led_one.on()
#     time.sleep(10)
#     led_one.off()
