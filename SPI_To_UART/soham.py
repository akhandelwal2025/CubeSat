import spidev
import threading
import RPi.GPIO as GPIO


def main():
    global spi
    print("1")

    spi = spidev.SpiDev()
    spi.open(0, 1)
    spi.max_speed_hz = 9600

    x = input("What UART?")
    returnArray = readUART(x)
    print(returnArray)


def readUART(numOfUART):
    spi.cshigh = False
    hexCC = []
    if numOfUART == 1:
        hexCC.append(0x11)
    elif numOfUART == 2:
        hexCC.append(0x12)
    elif numOfUART == 3:
        hexCC.append(0x13)
    else:
        hexCC.append(0x14)
    numOfBytes = spi.writebytes(hexCC)

    if numOfBytes == 1:
        hexCC.append(0x21)
    elif numOfBytes == 2:
        hexCC.append(0x22)
    elif numOfBytes:
        hexCC.append(0x23)
    else:
        hexCC.append(0x24)
    listOfVals = []
    try:
        for x in range(numOfBytes):
            currentVal = spi.readBytes(1)
            listOfVals.append(currentVal)
    except:
        print("Fuck")

    spi.cshigh = True;
    return listOfVals


main()
