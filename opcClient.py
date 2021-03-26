import time
import OpenOPC
import pywintypes

pywintypes.datetime = pywintypes.TimeType

opc = OpenOPC.client()
opc.connect(opc.servers()[0],'localhost')
opc.list()
print(opc.properties('ArduinoSerial0.Ze.Int1'))

while True:
    TAG = opc.properties('ArduinoSerial0.Ze.Int1')
    print(TAG[0][2])
    print(TAG[2])
    time.sleep(0.5)
else:
    opc.close()
