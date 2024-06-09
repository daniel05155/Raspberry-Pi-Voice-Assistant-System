import Adafruit_DHT
import csv
import datetime, time
import RPi.GPIO as GPIO
from gpiozero import DigitalOutputDevice

sensor = Adafruit_DHT.DHT22
dht_pin = 26        # GPIO PIN Num.
fan_pin = 14 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dht_pin, GPIO.OUT)
GPIO.setup(fan_pin, GPIO.OUT)

def run():
    GPIO.setmode(GPIO.BCM)
    dev = DigitalOutputDevice(fan_pin, active_high=True)
    with open('../dht.csv', 'a') as dhtfile:
        dhtwriter = csv.writer(dhtfile, dialect='excel')
        try:
            while True:
                humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
                if humidity is not None and temperature is not None:
                    now_time=datetime.datetime.now().strftime('%y %m %d %H-%m-%S')
                    dhtwriter.writerow(['Time:{}'.format(now_time),
                                        '\tTemp:{:0.1f}C'.format(temperature),
                                        '\tHumidity:{:0.1f}%'.format(humidity)])
                    print('溫度：{0:0.1f}C 溼度：{1:0.1f}%'.format(temperature, humidity))
                    if temperature>=28:
                        dev.on()
                        print('========== Turn on the fan ==========')
                    else:
                        dev.off()
                else:
                    print('Failed to get reading. Try again!')
                time.sleep(3)
        except KeyboardInterrupt:
            pass

if __name__=='__main__':
    run()
