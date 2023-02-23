# Instalação do Kaspersky em dispositivos Debian

## Verificando a existencia do arquivo locale en_US
### Essa verificação é importante pois ao tentar realizar a instalação sem um locale presente na lista de instalação retorna o erro "xx_XX is not a valid locale"

Utilize do comando locale para avaliar se o dispositivo ja o possui

```bash
locale -a
```

Caso o dispositivo não possua utilize do seu gerenciador de texto preferido para abrir a lista de locais

```bash
nano /etc/locale.gen
```
Vá para o final do arquivo e adicione a seguinte linha e em seguida salve o mesmo

```bash
en_US.UTF-8 UTF-8
```

Utilize do comando a seguir para executar a instalação do novo local

```bash
locale-gen
```
## Realizando a instalação do Endpoint
### Realize o download do kesl.deb na página de instalação da Kaspersky

Utilize do comando dpkg-i para instalar o kaspersky a partir do arquivo na máquina

```bash
dpkg -i kesl(versão).deb
```

Após finalizar a instalação utilize do seguinte comando para iniciar o script de post install
```bash
cd /opt/kaspersky/kesl/bin/
./kesl-setup.pl
```
Aceite o EULA e os termos de uso do Kaspersky Security Network (KSN) e em seguida configure o usuário que terá o papel de administrador do endpoint no dispositivo
