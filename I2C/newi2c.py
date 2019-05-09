import time
from smbus2 import SMBusWrapper
address = 0x08

time.sleep(2)

while True:
    message_to_send = input("Enter a message to send:")
    message_to_send = [message_to_send]
    data_received = 0
    with SMBusWrapper as bus:
        bus.write_i2c_block_data(address, 0x01, message_to_send)
        while True:
            data = bus.read_i2c_block_data(address, 0x02)
            if data != None:
                break
    print(f"Data Received: {data}")
    

