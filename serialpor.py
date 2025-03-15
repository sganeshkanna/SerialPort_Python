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


def convert():
    line = '2A8000080505434F4D504C4554458123'
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




    except Exception as e:
        print(e)

        pass
