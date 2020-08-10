import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import filedialog
import sys
txt,file_path = "",""
baud = 9600 #Set to 1200 if using PC-1350/60
def loadPort():
    i=0
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in ports:
            print("["+str(i)+"] {}: {} [{}]".format(port, desc, hwid))
            i+=1
    val = input("Enter port number [x]: ")

    try:
        port = "\\\\.\\"+ports[int(val)][0]
        return port
    except:
        print("Invalid port #\n")
        loadPort()

def connectSerial(port):
    try:
        return serial.Serial(port, baud, timeout=None, parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    except Exception as e:
        print(str(e)+"\n")
        loadPort()

def loadAndSend(ser):
    if(len(sys.argv) >1):
        filename=str(file_path).split('/')[-1]
        file_path=sys.argv[1]
        print("Loaded "+str(filename))
    else:
        print("Select your file:")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
    with open(file_path, encoding='utf-8') as file:
        data = file.read()
        print("Encoding and sending: "+str(file_path).split('/')[-1], end="... ")
        if(not "" in data):
            print("[1A EOF terminator not detected in file, adding it]")
            data = data+""
        try:
            x = ser.write(str.encode(data))
            print(str(x)+" bytes sent..",end=" ")
            ser.close()
            print("Complete.")
        except Exception as e:
            print(e)
        

port = loadPort()
ser = connectSerial(port)
print("\nConnected Successfully")
loadAndSend(ser)
