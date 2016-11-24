import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
b = 0
i = 0
f = 0
while True:
        arduino = float(ser.readline())
        if arduino == 0:
                i = 0
                f = 0
                if b == 0:
                        b = 1
                        print("Todo Bien")
        elif arduino == 1:
                b = 0
                f = 0
                if i == 0:
                        i = 1
                        print("Hay un Intruso")
                        import Iuri
                        import Iely
        elif arduino == 2:
                b = 0
                i = 0
                if f == 0:
                        f = 1
                        print ("Hay un Incendio")
                        import Furi
                        import Fely
