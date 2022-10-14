#!/bin/python3
# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
import os
import time

sistema = (struct.calcsize("P") * 8)
if sistema == 64:
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IP]"')
    time.sleep(5.0)
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')
    
if sistema == 32:
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IP]"')
    time.sleep(5.0)
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')

else:
    print("Seu dispositivo não possuí agente de rede instalado")