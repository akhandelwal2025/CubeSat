import spidev

def main():
    global spi
    print("1")
    
    spi = spidev.SpiDev()
    
    spi.open(0,1)
    spi.max_speed_hz = 9600
    spi.cshigh = False
    spi.writebytes([0x80, 3])
    #spi.writebytes([0x40, 2, 4])
    spi.writebytes([0x42, 2, 5])
    #spi.xfer([0x42, 2, 3])
    spi.writebytes2([])
    spi.writebytes([0x22])
    print(spi.readbytes(34))
    spi.cshigh = True
#    x = input("What UART?")
#    returnArray = readUART(1)
#    print(returnArray)


def readUART(numOfUART):
    spi.cshigh = False
    hexCC = []
    if numOfUART == 1:
        hexCC.append(0x21)
    elif numOfUART == 2:
        hexCC.append(0x22)
    elif numOfUART == 3:
        hexCC.append(0x23)
    else:
        hexCC.append(0x24)
    numOfBytes = spi.xfer(hexCC)
    return numOfBytes
    

#    if (numOfBytes == 1):ßÍÍÍ
#        hexCC.append(0x21)
#    elif (numOfBytes == 2):
#        hexCC.append(0x22)
#    elif (numOfBytes):
#        hexCC.append(0x23)
#    else:
#        hexCC.append(0x24)    
#    listOfVals = []
#    try:
#        for x in range(numOfBytes.len()):
#            currentVal = spi.readbytes(1)
#            listOfVals.append(currentVal)
#    except:
#        print("Nani")
    
#    spi.cshigh = True;


main()
