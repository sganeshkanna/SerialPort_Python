import serial
import time



ack = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x01, 0x41, 0x43, 0x4B, 0x81, 0x23]
setting_ack = [0x2A, 0x80, 0x00, 0x03, 0x02, 0x01, 0x41, 0x43, 0x4B, 0x81, 0x23]
machineready_ack = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x04, 0x41, 0x43, 0x4B, 0x81, 0x23]
req = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x03, 0x52, 0x45, 0x51, 0x81, 0x23]


def convert():
    line = '2A80000301035245518123'
    n = 2
    print(['0x'+line[i:i + n] for i in range(0, len(line), n)])

serialPort = serial.Serial(
    port="COM10", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)





serialString = ""  # Used to hold data coming over UART
while 1:
    # Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()
    print(serialString)
    # Print the contents of the serial data
    try:
        received = serialString.decode("Ascii");
        print(received)
        if(received.__contains__('HANDSHAKE')):
            print('Sending ACK')
            serialPort.write(serial.to_bytes(ack))
            time.sleep(3)
            print('Sending REQ')
            serialPort.write(serial.to_bytes(req))
        elif (received.__contains__('|7:1$3|')):
            print('Sending setting ack')
            serialPort.write(serial.to_bytes(setting_ack))
        elif (received.__contains__('MACHINE READY')):
            serialPort.write(serial.to_bytes(machineready_ack))
            serialPort.flush()

    except:
        pass
