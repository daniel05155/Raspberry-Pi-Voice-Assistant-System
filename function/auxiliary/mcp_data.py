from gpiozero import MCP3008
import time
import spidev

light = MCP3008(0)

# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0,0)

# Read SPI data from MCP3008, Channel must be an integer 0-7 
def ReadADC(ch):
    if ((ch > 7) or (ch < 0)):
       return -1
    adc = spi.xfer2([1,(8+ch)<<4,0])
    data = ((adc[1]&3)<<8) + adc[2]
    return data

# Convert data to voltage level
def ReadVolts(data,deci):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,deci)
    return volts

if __name__ =='__main__':
    while True:
        # Sensor channel
        light_ch = 0
        # Read the resistance value
        light_data = ReadADC(light_ch)
        # Volt value
        light_volts = ReadVolts(light_data,2)
        print(f'Light:{light_data}, Light_Volt:{light_volts}')
        time.sleep(3)
