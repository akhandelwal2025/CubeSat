import spidev
import threading
import RPi.GPIO as GPIO

def main():
    global spi
    spi = spidev.SpiDev()
    spi.max_speed__hz = 9600

    spi.open(0,1)

def readUART(numOfUART):
    spi.xfer(0x0)

if __name__ == '__main()__':
    t1 = threading(target=main, args=(), daemon=True)
    t1.start()
    t1.join()