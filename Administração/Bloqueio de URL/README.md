placeholder guide bloqueio de url
# Guia para realizar o bloqueio de URL's nos endpoints geridos pelo seu KSC
> Tutorial para estar utilizando o módulo de Security Control -> Web Control a fim de realizar o bloqueio de URL's específicas

1. Acesse a parte de gerenciamento de políticas e selecione a política desejada no seu KSC

![alt text](https://github.com/JustHobbs/KasperskyGuide/blob/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Administra%C3%A7%C3%A3o/Bloqueio%20de%20URL/imagem01.png)

2. Aperte na política com o botão direito e em seguida aperte em propriedades para abrir a janela de gerenciamento da mesma

![alt text](https://github.com/JustHobbs/KasperskyGuide/blob/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Administra%C3%A7%C3%A3o/Bloqueio%20de%20URL/imagem02.png)

3. Ao acessar a janela de gerenciamento da política, você conseguirá encontrar várias seções, cada uma é relativa a uma funcionalidade da política daquele plugin. No caso para realizar o bloqueio de URL's é necessário acessar a parte de Security Controls, em seguida, acessar a parte de Web Control.

4. Seguiremos o processo para realizar o bloqueio de uma URL desejada. Ao acessar a parte de Web Control você vai se deparar com uma tela parecida com essa:

![alt text](https://github.com/JustHobbs/KasperskyGuide/blob/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Administra%C3%A7%C3%A3o/Bloqueio%20de%20URL/imagem1.png)

É notável que nesta tela existam três subseções: Web Control settings, Message template settings e Advanced settings.
>Web Control Settings - Área aonde será realizado o gerenciamento das páginas ou conteúdos web.
>Message template - Área aonde é possível padronizar mensagens de aviso, bloqueio ou contato ao administrador para aparecer ao usuário.
>Advanced settings - Área aonde é possível verificar o log de páginas permitidas (ao ativar essa função, todo o tráfego terá que ser descriptografado o que acarretará na performance da máquina).

Para a requisição em questão usaremos a área de Web Control Settings.

5. Aperte em +Add para configurar uma nova regra e Web Control

6. Configure um nome para a regra

![alt text](https://github.com/JustHobbs/KasperskyGuide/blob/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Administra%C3%A7%C3%A3o/Bloqueio%20de%20URL/imagem03.png)

7. Em seguida você perceberá 5 abas que aparecem na regra. Irei explicar cada uma delas:
- Filter content 
> É divido em: Any Content (Bloqueará qualquer conteúdo), By Content Categories (Bloqueará de acordo com as categorias presentes e selecionadas nessa regra, exemplo: Conteúdos Violentos, Conteúdos Pornográficos, Sites de Apostas), By Types of Data (Bloqueará de acordo com o tipo de dado presente e selecionado nessa regra, exemplo: Vídeos, Fotos, Música) e By Content Categories and Types of Data (Bloqueará de acordo com as duas regras anteriores)
- Apply to addresses 
> Nessa subseção é possível especificar se vamos bloquear todas as URL's (utilizar esse modo caso utilize o By Content Categories ou o By Types of Data na seção anterior) ou se bloquearemos somente URL's específicas. Respectivamente: To all addresses ou To individual adresses
- Apply to users 
> Nessa subseção é possível especificar se vamos bloquear para todos os usuários ou para usuários específicos (como por exemplo, ao bloquear algum site de download de drivers no ambiente, se a equipe de TI do local solicitar e for aprovado é necessário mantê-los como exceção), para selecionar um usuário específico você deve estar conectado no AD para observar a máquina em questão.  Respectivamente: To all users ou To individual users and groups. 
- Action 
> A ação que será tomada pelo Kaspersky caso o site acessado "Trigge" essa regra: Allow (Permitir o acesso), Deny (Bloquear o acesso) e Warn (Uma mensagem de aviso será apresentada)
- Rule schedule 
> Nessa subseção é possível definir o horário que esta regra será aplicada (Por default: Always

## Exemplo de política de bloqueio a URL de sites pornográficos específicos:

![alt text](https://github.com/JustHobbs/KasperskyGuide/blob/Corre%C3%A7%C3%A3o-Dispositivos-Sem-Dados/Administra%C3%A7%C3%A3o/Bloqueio%20de%20URL/imagem04.png)
