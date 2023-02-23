# Kaspersky 

Além de prover segurança ao seu ambiente o antivírus Kaspersky pode ser utilizado para outras funções, tais como sua função de WSUS, prover acesso remoto nas máquinas e até gerencia de atualizações e vulnerabilidade.

## Instalação

Os arquivos para a instalação do mesmo 

# Alguns scripts para ajudar no dia-a-dia

## Sincronização
Com o intuito de corrigir alguns problemas de sincronização que aconteciam ocasionalmente fiz um script para ser executado diariamente nos dispositivos.

[Correção Sincronização](https://github.com/JustHobbs/KasperskyGuide/blob/Correção-Dispositivos-Sem-Dados/Scripts/Finalizados/SincronizarAoKSCv3_0.py)

## Correção de instalação
Com o objetivo de corrigir endpoints com o status de "sem dados do dispositivo" formulei esse script que identifica a versão do endpoint instalado e utiliza o código de reparo específico do mesmo.
O código de reparo foi obtido através do fórum da Kaspersky e contato com o fabricante

[Correção de Instalação](https://github.com/JustHobbs/KasperskyGuide/blob/Correção-Dispositivos-Sem-Dados/Scripts/Finalizados/CorrecaoSemDados.py)

## Remoção do Kaspersky Endpoint Agent
A partir da versão 11.8 do endpoint o KEA (Kaspersky Endpoint Agent) se tornou obsoleto então para realizar a desinstalação do mesmo em alguns dispositivos aonde a desinstalação via console não foi efetiva foi criado esse script que em muitos dos casos se mostrou como efetivo.

[Remoção KEA](https://github.com/JustHobbs/KasperskyGuide/blob/Correção-Dispositivos-Sem-Dados/Scripts/Finalizados/RemovedorAutomatizadoKEA.ps1)
