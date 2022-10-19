#!/bin/python3
import struct
import os
import time

KSC = "[IPCONSOLE]"
response = os.system("ping " + KSC)

# Checar conexão com o KSC
if response == 0:
  print(KSC, 'Conexão com o KSC okay')
else:
  print(KSC, 'Conexão com o KSC falhou utilizar o CGW!')


# Checar se o sistema é 64Bits ou 32Bits
sistema = (struct.calcsize("P") * 8)
if sistema == 64:
    print("Utilizar o diretório de 64x")
if sistema == 32:
    print("Utilizar o diretório de 32x")


#Sistema 64Bits e Conexão com o KSC estabelecida
if sistema == 64 and response == 0:
    os.system("net start klnagent")
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IPCONSOLE]"')
    time.sleep(20)
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')

#Sistema 32Bits e Conexão com o KSC estabelecida
if sistema == 32 and response == 0:
    os.system("net start klnagent")
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IPCONSOLE]"')
    time.sleep(20)
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')

#Sistema 64Bits e Conexão com o KSC falhou
if sistema == 64 and response == 1:
    os.system("net start klnagent")
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IPCGW]"')
    time.sleep(20)
    os.system('"start cmd /c ""C:\\Program Files (x86)\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')

#Sistema 32Bits e Conexão com o KSC falhou    
if sistema == 32 and response == 1:
    os.system("net start klnagent")
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klmover.exe"" -address [IPCGW]""')
    time.sleep(20)
    os.system('"start cmd /c ""C:\\Program Files\\Kaspersky Lab\\NetworkAgent\\klnagchk.exe"" -sendhb"')