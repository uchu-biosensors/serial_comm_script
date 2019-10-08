import sys
import os
import serial
import time

port = "/dev/ttyACM0"
baudrate = 9600

ser = serial.Serial(port, baudrate)

def receive():
    data = ser.read_until()
    data_string = data.decode('ascii')
    return data_string

def transmit(msg):
    if (type(msg) is int):
        msg = str(msg) + '\n'
    elif (type(msg) is str):
        msg = msg + '\n'
    msg_encoded = msg.encode('ascii')
    ser.write(msg_encoded)

# Get input, read data, close file on keyboard interrupt
try:
    # Get file name, open to append and create if file doesn't exist
    filename = raw_input("Please enter a file name (don't forget .csv): ")
    with open(filename, "a+") as f:
        # CSV header titles for importing to Excel
        f.write("Time (ms),Vsd (ADC),V+ (ADC),Vout (ADC),Isd (ADC),Temp (ADC),Gnd (ADC),")
        f.write("Vsd (mV),V+ (mV),Vout (mV),Isd (mV),Temp (mV),Gnd (mV)\n")
        start_time = int(round(time.time() * 1000))
        # Accept user input to pass to Arduino if appropriate, if not append data to CSV
        while True:
            ard_msg = receive();
            ard_msg_decoded = ard_msg.decode('ascii')
            print(ard_msg_decoded), 
            if ard_msg_decoded[:1] == 'E':
                res = raw_input()
                transmit(res)
            elif ard_msg_decoded[:1] == 'W':
                res = raw_input()
                transmit(res)
            else:
                ard_msg_decoded = ',' + ard_msg_decoded
                ard_msg_decoded = str((int(round(time.time() * 1000))) - start_time) + ard_msg_decoded
                f.write(ard_msg_decoded)
# Stop program, tell Arduino to "stop", and exit program on Ctrl + C
except KeyboardInterrupt:
    print("\n\nStopping program\n\n")
    transmit("stop")
    f.close()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
