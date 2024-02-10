import serial

ser = serial.Serial("COM11", 9600, timeout = 1) #Change your port name COM... and your baudrate

def retrieveData():
    ser.write(b'1')
    data = ser.readline().decode('ascii')
    return data

def retrieveData1():
    ser.write(b'2')
    data = ser.readline().decode('ascii')
    return data

def retrieveData2():
    ser.write(b'3')
    data = ser.readline().decode('ascii')
    return data

def retrieveData3():
    ser.write(b'4')
    data = ser.readline().decode('ascii')
    return data

def retrieveData4():
    ser.write(b'5')
    data = ser.readline().decode('ascii')
    return data

def retrieveData5():
    ser.write(b'6')
    data = ser.readline().decode('ascii')
    return data

while(True):
    uInput = input("Retrieve data? ")
    if uInput == '1':
        print(retrieveData())
    elif uInput == '2':
        print(retrieveData1())
    elif uInput == '3':
        print(retrieveData2())
    elif uInput == '4':
        print(retrieveData3())
    elif uInput == '5':
        print(retrieveData4())
    elif uInput == '6':
        print(retrieveData5())
