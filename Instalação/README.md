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
´´´
