import serial
import time
data = serial.Serial(
                    'COM7',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )



def finger():
    while True:
        print("taking")
        Data = data.readline().decode('utf-8', 'ignore').strip()
        print(Data)

        if Data in ["A", "B", "C", "D"]:
            break

    return Data

