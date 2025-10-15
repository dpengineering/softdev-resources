from dpeaDPi.DPiComputer import DPiComputer
from time import sleep

dpiComputer = DPiComputer()
dpiComputer.initialize()

#
# This example reads the "SIG" pin of connector "IN 0-3"
#
print("Digital input example:")

try:
    while True:
        in0 = dpiComputer.readDigitalIn(dpiComputer.IN_CONNECTOR__IN_0)
        in1 = dpiComputer.readDigitalIn(dpiComputer.IN_CONNECTOR__IN_1)
        in2 = dpiComputer.readDigitalIn(dpiComputer.IN_CONNECTOR__IN_2)
        in3 = dpiComputer.readDigitalIn(dpiComputer.IN_CONNECTOR__IN_3)
        print(f"{in0}, {in1}, {in2}, {in3}")
        sleep(.1)

except KeyboardInterrupt:
    print("Caught keyboard interrupt")