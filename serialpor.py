import serial
import time



ack = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x01, 0x41, 0x43, 0x4B, 0x81, 0x23]
setting_ack = [0x2A, 0x80, 0x00, 0x03, 0x02, 0x01, 0x41, 0x43, 0x4B, 0x81, 0x23]
machineready_ack = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x04, 0x41, 0x43, 0x4B, 0x81, 0x23]
req = [0x2A, 0x80, 0x00, 0x03, 0x01, 0x03, 0x52, 0x45, 0x51, 0x81, 0x23]
receipt_ack = [0x2A, 0x80, 0x00, 0x03, 0x05, 0x01, 0x41, 0x43, 0x4B, 0x81, 0x23]
ready = [0x2A, 0x80, 0x00, 0x05, 0x05, 0x02, 0x52, 0x45, 0x41, 0x44, 0x59, 0x81, 0x23]
current_mm = [0x2A, 0x80, 0x00, 0x02, 0x05, 0x03, 0x31, 0x31, 0x81, 0x23]
current_passage = [0x2A, 0x80, 0x00, 0x01, 0x05, 0x03, 0x31, 0x81, 0x23]
process_complete = [0x2A, 0x80, 0x00, 0x08, 0x05, 0x05, 0x43, 0x4F, 0x4D, 0x50, 0x4C, 0x45, 0x54, 0x45, 0x81, 0x23]
cancel_ack = [0x2A, 0x80, 0x00, 0x03, 0x05, 0x06, 0x41, 0x43, 0x4B, 0x81, 0x23]
reset_ack = [0x2A, 0x80, 0x00, 0x03, 0x05, 0x07, 0x41, 0x43, 0x4B, 0x81, 0x23]
reset_complete = [0x2A, 0x80, 0x00, 0x08, 0x05, 0x08, 0x43, 0x4F, 0x4D, 0x50, 0x4C, 0x45, 0x54, 0x45, 0x81, 0x23]
exponentaial_ack = [0x2A, 0x80, 0x00, 0x03, 0x02, 0x02, 0x41, 0x43, 0x4B, 0x81, 0x23]
exponential_data = [0x2A, 0x80, 0x00, 0x55, 0x02, 0x03, 0x31, 0x3A, 0x34, 0x30, 0x2E, 0x30, 0x30, 0x7C, 0x32, 0x3A, 0x33, 0x38, 0x2E, 0x37, 0x36, 0x7C, 0x33, 0x3A, 0x33, 0x37, 0x2E, 0x35, 0x36, 0x7C, 0x34, 0x3A, 0x33, 0x36, 0x2E, 0x33, 0x39, 0x7C, 0x35, 0x3A, 0x33, 0x35, 0x2E, 0x32, 0x36, 0x7C, 0x36, 0x3A, 0x33, 0x34, 0x2E, 0x31, 0x34, 0x7C, 0x37, 0x3A, 0x33, 0x33, 0x2E, 0x31, 0x31, 0x81, 0x23]



def convert():
    line = '2A8000550203313A34302E30307C323A33382E37367C333A33372E35367C343A33362E33397C353A33352E32367C363A33342E31347C373A33332E31318123'
    n = 2
    print(['0x'+line[i:i + n] for i in range(0, len(line), n)])

serialPort = serial.Serial(
    port="COM10", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)


convert()


serialString = ""  # Used to hold data coming over UART
while 1:
    # Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()
    print(serialString)
    # Print the contents of the serial data
    try:
        # received = serialString.decode("Ascii")
        # print(received)
        if(serialString.__eq__(b'')):
            pass
        elif(serialString.__contains__(b'HANDSHAKE')):
            print('Sending ACK')
            serialPort.write(serial.to_bytes(ack))
            time.sleep(3)
            print('Sending REQ')
            serialPort.write(serial.to_bytes(req))
        elif (serialString.__contains__(b'|7:1')):
            print('Sending setting ack')
            serialPort.write(serial.to_bytes(setting_ack))
        elif (serialString.__contains__(b'MACHINE READY')):
            print('Sending machine ready ack')
            serialPort.write(serial.to_bytes(machineready_ack))
        elif (serialString.__contains__(b'\x05\x011')):
            print('Sending receipt ack')
            serialPort.write(serial.to_bytes(receipt_ack))
            time.sleep(3)
            print('Sending ready')
            serialPort.write(serial.to_bytes(ready))
            time.sleep(3)
            print('Sending current mm')
            serialPort.write(serial.to_bytes(current_mm))
            time.sleep(3)
            print('Sending current passage')
            serialPort.write(serial.to_bytes(current_passage))
            time.sleep(3)
            print('Sending process complete')
            serialPort.write(serial.to_bytes(process_complete))
        elif (serialString.__contains__(b'CANCEL')):
            print('Sending cancel ack')
            serialPort.write(serial.to_bytes(cancel_ack))
        elif (serialString.__contains__(b'RESET')):
            print('Sending RESET ack')
            serialPort.write(serial.to_bytes(reset_ack))
            time.sleep(3)
            print('Sending reset complete')
            serialPort.write(serial.to_bytes(reset_complete))
        elif (serialString.__contains__(b'\x02\x02')):
            print('Sending Exponential data ack')
            serialPort.write(serial.to_bytes(exponentaial_ack))
            time.sleep(3)
            print('Sending exponential data ')
            serialPort.write(serial.to_bytes(exponential_data))




    except Exception as e:
        print(e)

        pass
