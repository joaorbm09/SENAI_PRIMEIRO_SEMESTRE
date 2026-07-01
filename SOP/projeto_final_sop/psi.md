# 🛡️ Política de Segurança da Informação (PSI)

<p align="center">
  <img src="https://img.shields.io/badge/Empresa-InovaTech%20Solu%C3%A7%C3%B5es-blue?style=for-the-badge" alt="InovaTech Soluções">
  <img src="https://img.shields.io/badge/Vers%C3%A3o-1.0-green?style=for-the-badge" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/Data-Junho%20de%202026-orange?style=for-the-badge" alt="Junho de 2026">
</p>

---

## 👥 Público-Alvo
Esta política aplica-se obrigatoriamente a:
* Todos os colaboradores e funcionários internos.
* Administradores de sistemas e equipes de infraestrutura.
* Prestadores de serviço, consultores e usuários remotos.

---

## 1. Objetivos e Escopo

### 1.1. Objetivos
Esta Política de Segurança da Informação (PSI) estabelece as diretrizes normativas para proteger os ativos de informação da **InovaTech Soluções**. O objetivo é mitigar riscos cibernéticos, estabelecer o uso aceitável dos recursos tecnológicos e garantir a total conformidade com:
* **LGPD** (Lei Geral de Proteção de Dados - Lei nº 13.709/18)
* **Marco Civil da Internet** (Lei nº 12.965/14)

### 1.2. Escopo
Aplica-se obrigatoriamente a todos os funcionários, prestadores de serviço e consultores que interagem com a infraestrutura de rede da empresa, em especial ao servidor corporativo baseado no sistema operacional **Debian 12 (Bookworm)**.

---

## 2. Governança e Segurança da Infraestrutura (Servidor Debian 12)

A sustentação tecnológica desta política baseia-se em controles rígidos implementados no servidor central, mapeados conforme as exigências legais:

### 2.1. Política de Controle de Acesso e Elevação de Privilégios
* **Trilha de Auditoria:** É terminantemente proibido o login direto como usuário `root` via console local ou conexões remotas. Todo acesso administrativo deve iniciar por um usuário comum devidamente identificado e, quando necessário, elevado via comando `su`.
* **Justificativa Legal:** Essa prática atende às exigências de responsabilização e transparência na governança de dados pessoais, permitindo identificar com precisão o operador responsável por qualquer alteração no sistema.

### 2.2. Postura de Perímetro e Firewall Ativo (UFW)
A InovaTech Soluções adota o princípio do *Privilégio Mínimo* em sua rede por meio do utilitário **Uncomplicated Firewall (UFW)**:

* **Postura Restritiva Padrão:** O tráfego de entrada é configurado como negação absoluta (`ufw default deny incoming`), garantindo que apenas tráfegos explicitamente homologados acessem o servidor.
* **Mitigação de Ataques Automatizados:** A porta de gerência SSH (`22/TCP`) opera sob a diretriz de limitação de taxa de conexão (`ufw limit ssh`). Caso um terminal externo realize tentativas consecutivas de conexões em curto espaço de tempo (ataque de força bruta), a origem é temporariamente bloqueada.

#### Serviços Autorizados e Portas Liberadas:

| Serviço | Protocolo / Porta | Descrição / Escopo |
| :--- | :--- | :--- |
| **Samba** | UDP 137, 138<br>TCP 139, 445 | Servidor de Arquivos Corporativo (Tráfego Restrito) |
| **Web HTTPS** | TCP 443 | Tráfego Web Criptografado protegido por SSL/TLS |

---

## 3. Diretrizes de Acesso Remoto e Criptografia (VPN)

Com o aumento do modelo de trabalho remoto, o perímetro de segurança da InovaTech estende-se à residência dos colaboradores:

* **Obrigatoriedade do Túnel Seguro:** Todo e qualquer acesso aos arquivos internos compartilhados no Samba ou painéis web fora das dependências físicas da empresa deve ser realizado, obrigatoriamente, por meio da solução **OpenVPN** implementada.
* **Segurança em Trânsito (LGPD Art. 6º, VII - Princípio da Segurança):** O uso da VPN garante que os dados em trânsito sejam completamente cifrados. Fica expressamente proibido o tráfego de informações corporativas ou dados pessoais de clientes em canais abertos ou redes Wi-Fi públicas sem a ativação prévia do cliente OpenVPN.

---

## 4. Uso Aceitável dos Recursos de TI e Políticas de Senhas

> ⚠️ **Atenção:** Os computadores, contas de e-mail e acessos ao servidor fornecidos pela empresa devem ser utilizados **estritamente para fins profissionais**. É proibida a instalação de softwares não homologados pela TI.

### Requisitos de Complexidade de Credenciais (Senhas Comuns e VPN):
* **Comprimento Mínimo:** 12 caracteres.
* **Complexidade Obrigatória:** Letras maiúsculas, letras minúsculas, números e caracteres especiais.
* **Ciclo de Expiração:** Alteração obrigatória a cada **90 dias**.

---

## 5. Adequação Jurídica e Conformidade Legal

### 5.1. Alinhamento com a LGPD (Lei nº 13.709/2018)
* **Retenção Legítima e Descarte:** Dados pessoais tratados e armazenados no servidor Samba devem cumprir uma finalidade legítima. Dados que perderem sua utilidade legal devem ser eliminados de forma definitiva (ex: através do utilitário `shred` no Debian).
* **Segregação de Funções:** Os compartilhamentos de rede do Samba devem ser organizados por grupos de usuários. Um colaborador do setor de *Vendas* não pode ter privilégios de leitura na pasta do setor de *Recursos Humanos*, cumprindo o **Princípio da Necessidade (Art. 6º, III da LGPD)**.

### 5.2. Alinhamento com o Marco Civil da Internet (Lei nº 12.965/2014)
* **Guarda de Registros de Acesso (Art. 15):** A InovaTech Soluções, na condição de administradora de sistema autônomo, configura o subsistema de auditoria do Debian 12 para reter os logs de conexões (endereço IP de origem, data, hora e portas de destino) por um período mínimo de **6 meses**.
* **Sigilo das Comunicações:** Os logs gerados pelo firewall e pelo OpenVPN são confidenciais e armazenados em diretórios restritos do sistema, acessíveis apenas pela equipe de administração de infraestrutura autenticada.

---

## 6. Plano de Conscientização e Aculturamento

Visto que o elo humano é frequentemente o alvo de ataques de Engenharia Social, a InovaTech Soluções estabelece um programa contínuo de treinamento dividido em três pilares:

 1. **Integração (Onboarding):** Todo novo colaborador admitido deve passar obrigatoriamente por um alinhamento de segurança, onde aprenderá a utilizar o cliente OpenVPN e compreenderá as regras de segurança do Samba.
 2. **Simulações de Phishing Periódicas:** A equipe de segurança realizará testes controlados de Engenharia Social (e-mails falsos com iscas) **a cada trimestre**. Colaboradores que apresentarem comportamento de risco (clicar no link ou fornecer dados fictícios) serão direcionados a uma reciclagem educativa imediata.
 3. **Comunicação Mensal ("Pílulas de Segurança"):** Envio de informativos rápidos nos canais internos da empresa sobre prevenção a malwares, cuidados com Engenharia Social por telefone/aplicativos de mensagem e boas práticas na custódia de senhas.

---

## 🚨 7. Penalidades e Sanções

O descumprimento voluntário ou por negligência grave das normas contidas nesta PSI constitui falta grave. O colaborador estará sujeito a penalidades progressivas:

* [ ] Advertência formal por escrito.
* [ ] Suspensão temporária das credenciais de acesso remoto (VPN) e local.
* [ ] Demissão por **justa causa**, em conformidade com a Consolidação das Leis do Trabalho (CLT), além de eventuais ações de reparação civil por perdas e danos em caso de vazamento de dados que gerem multas à empresa perante a ANPD.