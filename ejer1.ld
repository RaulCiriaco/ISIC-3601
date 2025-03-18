LDmicro0.2
MICRO=Atmel AVR ATmega328 32-Pin packages
CYCLE=10000 us at Timer1, YPlcCycleDuty:0, ConfigurationWord(s):0xE5FBFF2700000000
CRYSTAL=16000000 Hz
BAUD=9600 Hz, RATE=1000000 Hz, SPEED=100000 Hz
COMPILED=C:\Users\THINKL13\Desktop\SistemasProgramables\prueba1.hex
COMPILER=IHEX

PULL-UP LIST
    PB: 0xFFFFFFFF 
    PC: 0xFFFFFFFF 
    PD: 0xFFFFFFFF 
END

VAR LIST
END

IO LIST
    XX1 at 11 0 0
    Yled1 at 16 0 0
END

PROGRAM
RUNG 1
  CONTACTS XX1 0 0
  COIL Yled1 0 0 0 0
END
