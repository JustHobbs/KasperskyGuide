# Indice
[Instalação do Kaspersky em dispositivos Debian](https://github.com/JustHobbs/KasperskyGuide/tree/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Instala%C3%A7%C3%A3o#instala%C3%A7%C3%A3o-do-kaspersky-em-dispositivos-debian)
[Realizando a verificação do Locale en_US](https://github.com/JustHobbs/KasperskyGuide/tree/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Instala%C3%A7%C3%A3o#verificando-a-existencia-do-arquivo-locale-en_us)
[Realizando a instalação do Endpoint](https://github.com/JustHobbs/KasperskyGuide/tree/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Instala%C3%A7%C3%A3o#realizando-a-instala%C3%A7%C3%A3o-do-endpoint)
[Realizando a instalação do Agente de rede](https://github.com/JustHobbs/KasperskyGuide/tree/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Instala%C3%A7%C3%A3o#realizando-a-instala%C3%A7%C3%A3o-do-agente-de-rede)




# Instalação do Kaspersky em dispositivos Debian

## Verificando a existencia do arquivo locale en_US
> Essa verificação é importante pois ao tentar realizar a instalação sem um locale presente na lista de instalação retorna o erro "xx_XX is not a valid locale"

1. Utilize do comando locale para avaliar se o dispositivo ja o possui

```bash
locale -a
```

2. Caso o dispositivo não possua utilize do seu gerenciador de texto preferido para abrir a lista de locais

```bash
nano /etc/locale.gen
```
3. Vá para o final do arquivo e adicione a seguinte linha e em seguida salve o mesmo

```bash
en_US.UTF-8 UTF-8
```

4. Utilize do comando a seguir para executar a instalação do novo local

```bash
locale-gen
```
## Realizando a instalação do Endpoint
### Realize o download do kesl.deb na página de instalação da Kaspersky

1. Utilize do comando dpkg-i para instalar o kaspersky a partir do arquivo na máquina

```bash
dpkg -i kesl(versão).deb
```

2. Após finalizar a instalação utilize do seguinte comando para iniciar o script de post install
```bash
./opt/kaspersky/kesl/bin/kesl-setup.pl
```
3. Aceite o EULA e os termos de uso do Kaspersky Security Network (KSN) digitando **Y** e apertando **Enter** para continuar e em seguida configure o usuário que terá o papel de administrador do endpoint no dispositivo

4. Se tudo foi especificado corretamente a mensagem "This setup script completed successfully" será mostrada na tela

## Realizando a instalação do Agente de Rede
### Realize o download do klnagent.deb na página de instalação da Kaspersky
> A instalação do Agente de Rede acontece quando há a necessidade (e licenças) de administrar os endpoints de sua rede através de um Servidor de Administração
1. Utilize do comando dpkg-i para instalar o Agente de Rede a partir do arquivo na máquina

```bash
dpkg -i klnagent(versão).deb
```

2. Após finalizar a instalação utilize do seguinte comando para iniciar o script de post install
```bash
./opt/kaspersky/klnagent/lib/bin/setup/postinstall.pl
```

3. Aceite o EULA digitando **Y** e apertando **Enter** para continuar

4. Aponte o DNS ou o IP estático do servidor de administração KSC da rede

5. Aponte ou mantenha a porta padrão de conexão ao Servidor de administração

6. Aponte ou mantenha padrão a porta de SSL do Servidor de administração

7. Confirme se deseja ou não utilizar a SSL Encryption e aperte **Enter** para confirmar 

8. Confirme se deseja utilizar o Agente de Rede como Connection Gateway e aperte **Enter** para confirmar

9. Se tudo foi especificado corretamente a mensagem "Kaspersky Network Agent is installed" será mostrada na tela

10. Verifique se o agente de rede foi iniciado com o seguinte comando
```bash
service klnagent status
```
