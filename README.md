# SharpPC-Transfer
A simple program that transfers text file programs over to the Sharp Pocket PC series over serial.

Devices supported such as:  
PC-1600  
PC-E500 series  
PC-13xx series  
PC-1450 / 1475  
PC-E220  
PC-G8xx series  

With the PC-1350/60 needing a baudrate of 1200 (default 9600).  
For help on creating a cable to use for transfer, read http://www.silicium.org/forum/viewtopic.php?t=42285  
For the cable, I use a DSD TECH SH-U09C2 USB to TTL Adapter (Firmware must be reprogrammed, but that is explained on the forum post)

#### Requirements
* `pip install pyserial`

# Usage:
Launching the program will bring you to a list of ports to choose from, select one and then select your file.  
You may drag and drop the file you want to transfer onto the script (or pass as an argument) if you do not want to browse for a file.
