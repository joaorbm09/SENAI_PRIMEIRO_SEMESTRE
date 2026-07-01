# Instalação e Configuração do Ambiente

Relatório de implantação do servidor Debian 12 e configuração de segurança para a solução OpenVPN.

---

## Sumário
1. [Preparação do Sistema e Elevação de Privilégios](#1-preparação-do-sistema-e-elevação-de-privilegios)
2. [Atualização de Repositórios e Instalação de Pacotes](#2-atualização-de-repositórios-e-instalação-de-pacotes)
3. [Firewall e Segurança de Perímetro](#3-firewall-e-segurança-de-perímetro)
4. [Configuração da VPN](#4-configuração-da-vpn)

---

## 1. Preparação do Sistema e Elevação de Privilégios

### 1.1 Autenticação de Operador e Elevação para `root`

![Instalação e elevação de privilégios](<imagens/1/apt update.png>)

**Descrição:** Tela de console do Debian GNU/Linux 12 (Bookworm, kernel 6.1.0-49-amd64) mostrando o login do usuário comum `server` e a elevação para superusuário com `su`.

**Análise Técnica:** A elevação manual demonstra a prática de não permitir logins diretos como `root` via console ou SSH. Esse processo mantém a trilha de auditoria e garante que tarefas administrativas sejam realizadas com o mínimo de privilégios necessários.

---

## 2. Atualização de Repositórios e Instalação de Pacotes

### 2.1 Instalação do `curl`

![Instalação do curl](<imagens/2/instalando curl pra instalar VPN.png>)

**Descrição:** Execução dos comandos `apt update` e `apt install curl -y` com privilégios administrativos.

**Análise Técnica:** O `curl` é um utilitário essencial para ambientes administrativos, permitindo requisições HTTP/HTTPS via CLI, download de scripts e automação de integrações.

### 2.2 Instalação do OpenVPN

![Instalação do OpenVPN](<imagens/2/apt install openvpn.png>)

**Descrição:** Processo de instalação do pacote `openvpn` via APT, com configuração automática de links simbólicos no `systemd`.

**Análise Técnica:** O sistema cria o serviço `openvpn` como unit no `systemd`, garantindo a persistência do daemon após reinicializações.

---

## 3. Firewall e Segurança de Perímetro

### 3.1 Instalação do UFW

![Instalação do UFW](<imagens/3/apt ufw firewall.png>)

**Descrição:** Instalação do `ufw` com `apt install ufw -y`.

**Análise Técnica:** O utilitário cria os arquivos de configuração globais e o serviço `ufw.service`, permitindo o gerenciamento de regras no `systemd`.

### 3.2 Política de negação de entrada

![UFW deny incoming](<imagens/3/ufw deny.png>)

**Descrição:** Aplicação do comando `ufw default deny incoming`.

**Análise Técnica:** Essa política estabelece o princípio do *Default Deny*, bloqueando conexões de entrada não autorizadas.

### 3.3 Política de permissão de saída

![UFW allow outgoing](<imagens/3/ufw allow outgoing.png>)

**Descrição:** Aplicação do comando `ufw default allow outgoing`.

**Análise Técnica:** O comando permite que o servidor inicie conexões externas legítimas, como atualizações e consultas DNS.

### 3.4 Limitação de taxa no SSH

![UFW limit SSH](<imagens/3/ufw limit ssh.png>)

**Descrição:** Aplicação de `ufw limit ssh` para proteção contra ataques de força bruta.

**Análise Técnica:** A limitação reduz tentativas repetidas de conexão, bloqueando temporariamente origens suspeitas.

### 3.5 Liberação do Samba

![UFW allow Samba](<imagens/3/ufw allow samba.png>)

**Descrição:** Aplicação de `ufw allow Samba` para liberar portas de compartilhamento de arquivos.

**Análise Técnica:** O comando abre as portas UDP 137/138 e TCP 139/445 para uso interno do Samba.

### 3.6 Liberação do HTTPS

![UFW allow HTTPS](<imagens/3/ufw allow https.png>)

**Descrição:** Aplicação de `ufw allow https`.

**Análise Técnica:** A regra libera a porta 443/TCP para tráfego HTTPS seguro.

### 3.7 Ativação do firewall

![Ativação do firewall](<imagens/3/ativando firewall.png>)

**Descrição:** Comando `ufw enable` com confirmação de ativação e persistência no boot.

**Análise Técnica:** O UFW passa a aplicar regras automaticamente a cada inicialização.

### 3.8 Verificação do estado do UFW

![Status do UFW](<imagens/3/Confirmação de funcionamento e status firewall.png>)

**Descrição:** Saída de `ufw status verbose`, exibindo regras habilitadas e políticas ativas.

**Análise Técnica:** O relatório confirma o bloqueio padrão de entrada, com SSH limitado, Samba autorizado e HTTPS liberado.

---

## 4. Configuração da VPN

### 4.1 Ativação de roteamento IPv4

![Ativação do roteamento IPv4](<imagens/4/descomentando linha net.ipv4.png>)

**Descrição:** Edição de `/etc/sysctl.conf` para habilitar `net.ipv4.ip_forward = 1`.

**Análise Técnica:** O kernel passa a encaminhar pacotes entre interfaces, permitindo que clientes VPN acessem a rede local.

### 4.2 Permissão de execução do instalador

![Permissão de execução](<imagens/4/chmod - permissão de execução.png>)

**Descrição:** Execução de `chmod +x openvpn-install.sh`.

**Análise Técnica:** O bit de execução permite que o script de instalação do OpenVPN seja executado pelo sistema.

### 4.3 Início do instalador do OpenVPN

![Assistente OpenVPN](<imagens/4/openvpn acesso instalação.png>)

**Descrição:** Tela inicial do instalador interativo do OpenVPN.

**Análise Técnica:** O assistente identifica NAT e solicita o endereço público ou FQDN para conexão dos clientes.

### 4.4 Configuração do cliente OpenVPN Road Warrior

![Configuração do OpenVPN](<imagens/4/openvpn instalação.png>)

**Descrição:** Definição do IP de escuta `10.0.2.15`, protocolo UDP, porta 1194 e DNS Google.

**Análise Técnica:** O uso de UDP e a porta 1194 seguem as melhores práticas de desempenho para VPN.

### 4.5 Inspeção do arquivo de cliente OpenVPN

![Configuração do cliente OpenVPN](<imagens/4/acessando ssh vendo documento linux via windows.png>)

**Descrição:** Exibição do arquivo `/root/usuario_inovatech.ovpn`.

**Análise Técnica:** O arquivo contém diretivas de conexão e o certificado RSA de 2048 bits assinado pela CA local.

### 4.6 Validação de conectividade com Nmap

![Validação SSH](<imagens/4/validação do SSH.png>) ![Validação VPN](<imagens/4/vaidação da VPN.png>)

**Descrição:** Varredura de portas em `10.0.2.15`, verificando SSH, NetBIOS, Samba e OpenVPN.

**Análise Técnica:** O resultado confirma a eficácia do firewall e a disponibilidade do serviço OpenVPN.
