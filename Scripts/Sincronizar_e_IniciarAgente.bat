## Script to syncronize devices and start network agent that doesnt are listening to your KSC
## Script para sincronizar os dispositivos e iniciar o networka agent que não estão escutando o seu KSC

net start klnagent

## Script to syncronize devices that doesnt are listening to your KSC
## Script para sincronizar os dispositivos que não estão escutando o seu KSC

###x86 Version
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\NetworkAgent\klmover.exe"" -address {INSERT_KSCorGATEWAY_ID}
timeout 5
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\NetworkAgent\klnagchk.exe"" -sendhb

###x64 Version
start cmd /c ""C:\Program Files\Kaspersky Lab\NetworkAgent\klmover.exe"" -address {INSERT_KSCorGATEWAY_ID}
timeout 5
start cmd /c ""C:\Program Files\Kaspersky Lab\NetworkAgent\klnagchk.exe"" -sendhb
