This repository contains a python script to receive and transmit information between a Raspberry Pi and Arduino using serial communication. The protocol utilizes serial communication.

Instructions:

1. Run "python serialcomm.py" in the terminal
2. Enter the name of the file you would like to save data to, with a .csv extension
3. Enter the delay between samples you would like to use for data collection
4. Enter the format of data you'd like to log (ADC output, millivolt output, or both)
5. Let the program run
6. When you want to terminate the program, enter "Ctrl + C" on the keyboard

To view data:

** Make sure to safely power off the Pi before viewing data **

1. Remove SD card from Raspberry pi
2. Insert SD card into a computer with Excel or equivalent software
3. Navigate to the removeable Pi device in your computer's file manager
4. navigate to directory "root --> home --> pi --> Desktop --> isfet --> CSV_files"
5. Open the desired .csv file in your software of choice
6. ** Make sure to eject the Pi's SD card safely before removing **

Data is logged in the following formats:

ADC and millivolt:

  timestamp,vsd,vplus,vout,isd,temp,gnd

Both:

  timestamp,vsd_adc,vplus_adc,vout_adc,isd_adc,temp_adc,gnd_adc,vsd_mv,vplus_mv,vout_mv,isd_mv,temp_mv,gnd_mv
