# Relatório de Análise de Vulnerabilidades de Infraestrutura

Este repositório contém o diagnóstico de segurança e o plano de ação para o hardening do ambiente de servidores da InovaTech Soluções.

## 📋 Informações Gerais
* **Cliente:** InovaTech Soluções
* **Alvo:** Servidor de Arquivos Linux (Ambiente CLI)
* **Responsável:** Consultoria em Segurança da Informação (Sua Equipe)
* **Status:** Diagnóstico Concluído / Pronto para Implementação

---

## 🗺️ Sumário
1. [Objetivo do Diagnóstico](#1-objetivo-do-diagnóstico)
2. [Metodologia e Ferramentas CLI Utilizadas](#2-metodologia-e-ferramentas-cli-utilizadas)
3. [Vulnerabilidades Identificadas](#3-vulnerabilidades-identificadas)
4. [Detalhamento Técnico das Falhas (Evidências em CLI)](#4-detalhamento-técnico-das-falhas-evidências-em-cli)
5. [Plano de Ação e Recomendações (Próximas Etapas)](#5-plano-de-ação-e-recomendações-próximas-etapas)
6. [Plano de Melhorias Imediatas via CLI](#6-plano-de-melhorias-imediatas-via-cli)
7. [Alinhamento com Legislações Vigentes](#7-alinhamento-com-legislações-vigentes)
8. [Conclusão do Diagnóstico](#8-conclusão-do-diagnóstico)

---

## 1. Objetivo do Diagnóstico
Identificar brechas de segurança, portas abertas desnecessariamente, serviços vulneráveis e falhas de configuração no servidor Linux da **InovaTech Soluções**. O foco principal é mitigar riscos antes de abrir o servidor para acessos remotos devido ao modelo de *home office*.

---

## 2. Metodologia e Ferramentas CLI Utilizadas
Como o servidor opera estritamente em modo texto (CLI), foram utilizados comandos nativos do ecossistema Linux para a auditoria interna:

* `ss -tulpn` ou `netstat -tulpn`: Para listar todas as portas lógicas abertas e os serviços associados aguardando conexões.
* `ps aux`: Para auditar os processos ativos em segundo plano e identificar serviços desnecessários.
* **Análise do arquivo `/etc/ssh/sshd_config`**: Para verificar as diretivas de segurança do serviço de acesso remoto.
* `lynis audit system`: Ferramenta recomendada de auditoria de segurança em CLI que varre o sistema em busca de falhas de endurecimento (*hardening*).

---

## 3. Vulnerabilidades Identificadas

| ID | Vulnerabilidade | Impacto | Nível de Risco | Descrição Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **VUL-01** | Ausência de Firewall Ativo | Total | **Crítico** | Não há tabelas de regras (UFW/Iptables) ativas. Qualquer requisição externa em qualquer porta chega diretamente aos serviços do sistema. |
| **VUL-02** | Acesso SSH Exposto e Inseguro | Alto | **Alto** | O SSH está rodando na porta padrão (22) e permite login direto do usuário root. Facilita ataques de força bruta (*brute force*). |
| **VUL-03** | Samba (Compartilhamento) Exposto | Alto | **Alto** | As portas do Samba (139 e 445) estão acessíveis externamente sem a proteção de uma rede privada (VPN), expondo dados da empresa na internet. |
| **VUL-04** | Tráfego de Dados Não Criptografado | Médio | **Alto** | Colaboradores remotos acessam arquivos e serviços via canais não criptografados, permitindo interceptação de dados (*sniffing*) em redes públicas. |
| **VUL-05** | Ausência de Logs e Bloqueio Automático | Médio | **Médio** | O sistema não possui ferramentas como o *fail2ban* para bloquear IPs após sucessivas tentativas de login malformadas. |

---

## 4. Detalhamento Técnico das Falhas (Evidências em CLI)

### Evidência 01: Portas escutando na interface pública (`0.0.0.0`)
Ao executar o comando `ss -tulpn`, observou-se que o serviço Samba (`smbd`) e o SSH (`sshd`) estão ouvindo requisições de qualquer IP da internet:

```text
tcp   LISTEN   0   50      0.0.0.0:445   0.0.0.0:* users:(("smbd",pid=1234,fd=33))
tcp   LISTEN   0   128     0.0.0.0:22    0.0.0.0:* users:(("sshd",pid=5678,fd=3))
```

### Evidência 02: Permissão de Root no SSH
Ao inspecionar o arquivo de configuração do SSH com o comando:

```bash
grep "PermitRootLogin" /etc/ssh/sshd_config
```

foi identificada a seguinte configuração ativa:

```text
PermitRootLogin yes
```

Impacto: isso significa que um atacante só precisa adivinhar a senha do administrador para tomar controle total do servidor.

---

## 5. Plano de Ação e Recomendações (Próximas Etapas)

Para adequar a InovaTech Soluções às exigências de segurança e legislações vigentes, a consultoria recomenda:

* Configuração imediata do firewall (UFW/Iptables): bloquear todo o tráfego de entrada por padrão e permitir explicitamente apenas portas essenciais (como HTTPS e SSH modificado).
* Mudança de escopo do Samba: configurar o serviço para ouvir apenas na interface da rede local (127.0.0.1 ou IP da LAN), nunca no IP público da internet.
* Implementação de VPN (OpenVPN): garantir que o acesso remoto ocorra por túnel criptografado antes de ter acesso às pastas compartilhadas.
* Hardening do SSH: alterar a porta padrão (por exemplo, de 22 para 2222), desabilitar o `PermitRootLogin` e forçar o uso de chaves públicas/privadas em vez de senhas.

---

## 6. Plano de Melhorias Imediatas via CLI

Para sanar as vulnerabilidades apontadas no diagnóstico inicial, este plano de ação foca no hardening do sistema usando apenas ferramentas e comandos nativos em modo texto.

### 🛠️ M-01: Endurecimento (Hardening) do Serviço SSH
Para mitigar a vulnerabilidade VUL-02, aplicaremos restrições no arquivo de configuração do daemon SSH (`/etc/ssh/sshd_config`).

Ação: alterar a porta padrão e proibir o login direto do usuário root.

```bash
# 1. Altera a porta padrão de 22 para 2222
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 2. Desativa o login direto como root
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# 3. Reinicia o serviço para aplicar as alterações
sudo systemctl restart sshd
```

### 🗄️ M-02: Isolamento de Rede do Serviço Samba
Para mitigar a vulnerabilidade VUL-03, configuraremos o Samba para responder somente à rede local e à futura sub-rede da VPN.

Ação: editar `/etc/samba/smb.conf` e, no bloco `[global]`, adicionar:

```ini
[global]
interfaces = 127.0.0.1 192.168.1.0/24 10.8.0.0/24
bind interfaces only = yes
```

Nota técnica: `bind interfaces only = yes` garante que o Samba não abra as portas 139 e 445 para o IP público.

### 🛡️ M-03: Implementação de Sistema de Defesa Reativa (Fail2ban)
Para mitigar a vulnerabilidade VUL-05, instalaremos o `fail2ban`. Ele bloqueia IPs no firewall após tentativas de login suspeitas.

```bash
# Instalação do serviço via gerenciador de pacotes
sudo apt update && sudo apt install fail2ban -y

# Ativação do serviço para iniciar junto com o sistema
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

---

## 7. Alinhamento com Legislações Vigentes

As melhorias propostas não visam apenas a segurança técnica, mas também a conformidade jurídica da InovaTech Soluções:

* Marco Civil da Internet (Art. 15): exige a guarda de registros de acesso de forma segura e cronológica. Para dar validade jurídica aos logs, recomenda-se sincronizar a hora oficial via NTP.

```bash
sudo apt install chrony -y
sudo systemctl enable --now chrony
```

* LGPD (Lei Geral de Proteção de Dados): o isolamento do Samba e a criptografia da VPN protegem a confidencialidade dos dados pessoais de colaboradores e clientes, reduzindo o risco de vazamentos e acessos não autorizados.

---

## 8. Conclusão do Diagnóstico

Com a entrega deste relatório de vulnerabilidades e do respectivo plano de melhorias, a equipe está pronta para avançar. A aplicação desses comandos CLI servirá como base para que as próximas etapas (firewall e VPN) sejam implementadas sem herdar falhas de configuração do sistema operacional.