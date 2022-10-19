#!/bin/python3
# IMPORTS
from re import X
import struct
import os
import time
import subprocess
from unittest import result

### SEÇÃO PARA O ADMINISTRADOR
login = "InserirKLLOGIN"
password = "InserirPassword"

## TESTE PARA O ADMIN (DESCOMENTAR LINHA E VERIFICAR SE ESTÁ OK)
## COMENTAR O RESTO DO CODIGO AO REALIZAR O TESTE
#print('msiexec /i {305A9EC9-294E-4555-A7C5-E1C767E01C11} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 \lv*x path_to_log_file.txt /qn')

### IDENTIFICADOR DE VERSÃO
Versao = subprocess.check_output(['wmic', 'product', 'where', "name like 'Kaspersky Endpoint Security%'", 'get', 'version'])
print(Versao)


### COMANDOS DE CORREÇÃO
#KES11.10
KES11_10 = os.system('msiexec /i {305A9EC9-294E-4555-A7C5-E1C767E01C11} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 \lv*x path_to_log_file.txt /qn')
#KES11.9
KES11_9 = os.system('msiexec /i {6BB76C8F-365E-4345-83ED-6D7AD612AF76} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 /lv*x path_to_log_file.txt /qn')
#KES11.8
KES11_8 = os.system('msiexec /i {1F39E63E-3F9C-4E21-928B-136C6362E88B} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 /lv*x path_to_log_file.txt /qn')
#KES11.7
KES11_7 = os.system('msiexec /i {F4ECE08F-50E9-44E2-A2F3-2F3C8DDF8E16} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 /lv*x path_to_log_file.txt /qn')
#KES11.6
KES11_6 = os.system('msiexec /i {7EC66A9F-0A49-4DC0-A9E8-460333EA8013} KLLOGIN='+login+' KLPASSWD='+password+' REINSTALL=ALL REINSTALLMODE=amus EULA=1 PRIVACYPOLICY=1 SKIPREBOOTPENDING=1 /lv*x path_to_log_file.txt /qn')

## VERSÕES
a = ("11.10").encode()
b = ("11.9").encode()
c = ("11.8").encode()
d = ("11.7").encode()
e = ("11.6").encode()


### CORREÇÃO
if a in Versao:
    os.system('"start cmd /k "11.10" "')
    time.sleep(10)
    KES11_10
    input("com kaspersky")
if b in Versao:
    os.system('"start cmd /k "11.9" "')
    time.sleep(10)
    KES11_9
    input("com kaspersky")
if c in Versao:
    os.system('"start cmd /k "11.8" "')
    time.sleep(10)
    KES11_8
    input("com kaspersky")
if d in Versao:
    os.system('"start cmd /k "11.7" "')
    time.sleep(10)
    KES11_7
    input("com kaspersky")
if e in Versao:
    os.system('"start cmd /k "11.6" "')
    time.sleep(10)
    KES11_6
    input("com kaspersky")
else:
    input("sem kaspersky")
