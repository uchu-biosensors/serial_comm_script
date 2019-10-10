import sys
import os
import serial
import time

port = "/dev/ttyACM0"
baudrate = 9600
filepath = "../CSV_files/"

ser = serial.Serial(port, baudrate)
has_started = False

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
    filename = filepath + raw_input("Please enter a file name (don't forget .csv): ")
    with open(filename, "a+") as f:
        # CSV header titles for importing to Excel
        f.write("Time (sec),Vsd (ADC),V+ (ADC),Vout (ADC),Isd (ADC),Temp (ADC),Gnd (ADC),")
        f.write("Vsd (mV),V+ (mV),Vout (mV),Isd (mV),Temp (mV),Gnd (mV)\n")
        # Accept user input to pass to Arduino if appropriate, if not append data to CSV
        while True:
            ard_msg = receive();
            ard_msg_decoded = ard_msg.decode('ascii')
            if ard_msg_decoded[:1] == 'E':
                print(ard_msg_decoded), 
                res = raw_input()
                transmit(res)
            elif ard_msg_decoded[:1] == 'W':
                print(ard_msg_decoded), 
                res = raw_input()
                transmit(res)
            else:
                if (has_started != True):
                    has_started = True
                    start_time = round(float(time.time()), 3)
                # Add time to beginning of string
                ard_msg_decoded = ',' + ard_msg_decoded
                ard_msg_decoded = str(round(float(time.time() - start_time), 3)) + ard_msg_decoded
                print(ard_msg_decoded), 
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
