################################# README ################################
# Script criado com o intuito de remover o KEA quando a tarefa de remo��o
# n�o funciona.
# Utiliza o msiexec para realizar a remo��o atrav�s de GUID
#
#########################################################################


#Identificar a Versao e o GUID do Kaspersky Endpoint Agent
Write-host "Identificando o caminho do Kaspersky Endpoint Agent..."
$AppInfo = Get-WmiObject Win32_Product -Filter "Name Like '%Kaspersky Endpoint Agent%'"
$KeaVer = $AppInfo.Version
$GUID = $AppInfo.IdentifyingNumber
Write-host "Endpoint Agent est� na vers�o:" $KeaVer
Write-host "Endpoint Agent tem o GUID de:" $GUID


#Desinstalando usando o MSIEXEC
Write-host "Tentando desinstalar usando o MSIEXEC favor aceitar..."
& ${env:WINDIR}\System32\msiexec /x $GUID /Quiet /Passive /NoRestart