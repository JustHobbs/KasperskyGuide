## README ##
# Script criado com a função de solucionar os status: A proteção está desativada ou O aplicativo de segurança não está em execução
# O problema as vezes é ocasionado pois alguma falha aconteceu durante a inicialização e o endpoint não abriu
# Para solucionar isso o script força o inicio do endpoint no dispositivo


#x86
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\NetworkAgent\klpsm.exe"" start_avp_service
timeout 5
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\Kaspersky Endpoint Security for Windows\avpui.exe”"
timeout 5
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\NetworkAgent\klmover.exe"" -address InserirIP
timeout 5
start cmd /c ""C:\Program Files (x86)\Kaspersky Lab\NetworkAgent\klnagchk.exe"" -sendhb

x64
start cmd /c ""C:\Program Files\Kaspersky Lab\NetworkAgent\klpsm.exe"" start_avp_service
timeout 5
start cmd /c ""C:\Program Files\Kaspersky Lab\Kaspersky Endpoint Security for Windows\avpui.exe”"
timeout 5
start cmd /c ""C:\Program Files\Kaspersky Lab\NetworkAgent\klmover.exe"" -address InserirIP
timeout 5
start cmd /c ""C:\Program Files\Kaspersky Lab\NetworkAgent\klnagchk.exe"" -sendhb