# 🚗 QuickParking - Sistema de Gestão de Estacionamento

Sistema desenvolvido em Python para gerenciar o estacionamento de uma loja de conveniência localizada em um posto de combustível, realizando o controle de vagas, entrada e saída de veículos, cálculo automático de cobranças e geração de relatórios.

---

## 👥 Integrantes

- Beatriz Neves Bergamin
- João Wictor

---

## 📖 1. Introdução

### 1.1 Objetivo

O QuickParking tem como objetivo automatizar o gerenciamento de um estacionamento, permitindo o controle da ocupação das vagas, registro de veículos, cálculo automático de permanência, aplicação de regras de negócio e geração de relatórios administrativos.

### 1.2 Escopo

O sistema será responsável por:

- Controlar 20 vagas de estacionamento
- Registrar veículos estacionados
- Gerenciar entradas e saídas
- Calcular valores automaticamente
- Controlar a lotação do estacionamento
- Aplicar multas por estacionamento irregular
- Gerar relatórios financeiros
- Fornecer acesso administrativo

---

## 🖥️ 2. Visão Geral do Sistema

O QuickParking será desenvolvido em Python para auxiliar o controle operacional de um estacionamento de pequeno porte.

### 2.1 Capacidade do Estacionamento

- 20 vagas no total
- 15 vagas para carros, picapes e caminhões
- 5 vagas exclusivas para motocicletas

O sistema deverá monitorar a ocupação das vagas em tempo real, impedindo que a capacidade máxima seja ultrapassada.

### 2.2 Usuários do Sistema

**Operador**

Responsável por:

- Registrar entradas
- Registrar saídas
- Consultar vagas disponíveis
- Consultar veículos estacionados

**Administrador**

Responsável por:

- Consultar faturamento
- Gerar relatórios
- Visualizar movimentações
- Gerenciar informações do sistema

---

## 📋 3. Levantamento de Requisitos

### 3.1 Design Thinking

**Empatia**

Necessidades levantadas junto ao cliente:

- Controle de vagas ocupadas e livres
- Registro da placa dos veículos
- Controle de horários de entrada e saída
- Cobrança automática
- Controle de caminhões grandes
- Relatórios financeiros
- Aplicação de penalidades

**Brainstorming**

Funcionalidades identificadas:

- Cadastro de veículos
- Controle de lotação
- Controle de vagas
- Relatório diário
- Painel administrativo
- Sistema de multas
- Consulta de veículos estacionados
- Controle de horários

**Definição do Problema**

O estacionamento não possui um sistema automatizado para controlar a movimentação dos veículos, dificultando o gerenciamento das vagas e o cálculo das cobranças.

### 3.2 Briefing do Projeto

| Campo | Descrição |
|-------|-----------|
| **Nome** | QuickParking |
| **Cliente** | Loja de Conveniência de Posto de Combustível |
| **Problema** | Necessidade de controlar vagas, registrar veículos e calcular cobranças automaticamente |
| **Solução** | Desenvolvimento de um sistema em Python capaz de gerenciar todo o fluxo operacional do estacionamento |

---

## 👤 4. Histórias de Usuário

| ID | História |
|----|----------|
| US01 | Como operador, eu quero registrar a entrada dos veículos para controlar a ocupação das vagas. |
| US02 | Como operador, eu quero registrar a saída dos veículos para calcular automaticamente o valor devido. |
| US03 | Como cliente, eu quero ter gratuidade de até 15 minutos para realizar paradas rápidas. |
| US04 | Como administrador, eu quero visualizar o faturamento diário para acompanhar os resultados financeiros. |
| US05 | Como operador, eu quero visualizar vagas disponíveis para organizar melhor o estacionamento. |
| US06 | Como administrador, eu quero bloquear veículos acima de 12 metros para respeitar os limites físicos das vagas. |
| US07 | Como operador, eu quero identificar veículos estacionados irregularmente para aplicar penalidades. |

---

## ⚙️ 5. Requisitos Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RF01 | Registrar Entrada | O sistema deverá registrar placa, tipo do veículo, comprimento e data/hora de entrada. |
| RF02 | Questionário do Veículo | O sistema deverá solicitar o tipo do veículo (moto, carro, picape ou caminhão). Se caminhão, deverá informar o comprimento. |
| RF03 | Validar Comprimento | O sistema deverá impedir a entrada de veículos com comprimento superior a 12 metros. |
| RF04 | Controle de Vagas | O sistema deverá controlar 15 vagas para carros/picapes/caminhões e 5 vagas para motocicletas. |
| RF05 | Sinalização de Vagas | O sistema deverá exibir vagas ocupadas, vagas disponíveis e veículos estacionados. |
| RF06 | Controle de Lotação | O sistema deverá impedir novas entradas quando todas as vagas estiverem ocupadas. |
| RF07 | Registro de Saída | O sistema deverá registrar a saída do veículo e calcular o tempo de permanência. |
| RF08 | Cálculo Automático | O sistema deverá calcular automaticamente o valor da permanência. |
| RF09 | Horário de Funcionamento | O sistema deverá permitir entradas apenas entre 05:00 e 22:00. |
| RF10 | Aplicação de Multas | O sistema deverá registrar multas para veículos estacionados em locais não permitidos. |
| RF11 | Relatório Diário | O sistema deverá gerar relatórios com total de veículos, quantidade por tipo, total arrecadado e quantidade de multas. |

---

## 📌 6. Regras de Negócio

| Código | Regra |
|--------|-------|
| RN01 | Permanência de até 15 minutos é gratuita |
| RN02 | Primeira hora custa R$ 10,00 |
| RN03 | Cada hora adicional custa R$ 5,00 |
| RN04 | Capacidade máxima de 20 vagas |
| RN05 | Motocicletas ocupam apenas vagas destinadas a motos |
| RN06 | Veículos acima de 12 metros não podem entrar |
| RN07 | Todas as vagas possuem largura padrão de 2 metros |
| RN08 | Funcionamento das 05:00 às 22:00 |
| RN09 | Veículos em áreas proibidas recebem multa |

---

## 🔒 7. Requisitos Não Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RNF01 | Desempenho | O sistema deverá responder às operações em até 2 segundos. |
| RNF02 | Segurança | O acesso administrativo deverá exigir autenticação por usuário e senha. |
| RNF03 | Usabilidade | O sistema deverá possuir interface simples e intuitiva. |
| RNF04 | Confiabilidade | Os dados cadastrados deverão permanecer armazenados sem perda de informações. |
| RNF05 | Manutenibilidade | O código deverá utilizar funções, listas, dicionários e tratamento de exceções. |

---

## 🎨 8. Prototipação

A prototipação do sistema foi desenvolvida utilizando o Figma, com o objetivo de representar visualmente as funcionalidades do QuickParking antes da implementação.

Por meio do protótipo, foi possível planejar a disposição das informações, validar o fluxo de utilização do sistema e identificar possíveis melhorias na interface antes do desenvolvimento em Python.

### Protótipo do Sistema

![Protótipo QuickParking](https://github.com/user-attachments/assets/df07fbb2-f23d-4afc-bb21-7df2dd70c0b8)

---

## 🚀 9. Planejamento Ágil

### Kanban

O gerenciamento das atividades foi realizado por meio do GitHub Projects utilizando a metodologia Kanban. As atividades passaram pelas seguintes etapas:

| Etapa | Descrição |
|-------|-----------|
| **Backlog** | Registro inicial das tarefas planejadas |
| **A Fazer** | Atividades prontas para serem iniciadas |
| **Em Processo** | Documentação, prototipação e programação do sistema |
| **Review** | Revisão e validação das atividades |
| **Concluído** | Atividades finalizadas, como idealização e briefing |

### Scrum

**Sprint 1 (2 horas)**

- Idealização do projeto
- Briefing
- Levantamento de requisitos
- Design Thinking
- Histórias de Usuário
- Elaboração da ERS
- Organização do Kanban
- Início da documentação

> Sprint Review: Validação dos requisitos e documentação inicial.

**Sprint 2 (2 horas)**

- Continuação da documentação
- Desenvolvimento da prototipação no Figma
- Implementação em Python
- Testes e correções
- Relatórios financeiros

> Sprint Retrospective: A utilização das metodologias Scrum e Kanban contribuiu para a organização das atividades e acompanhamento do desenvolvimento do projeto.

---

## ✅ 10. Critérios de Aceitação

O sistema será considerado aprovado quando:

- [ ] Controlar corretamente as 20 vagas
- [ ] Diferenciar vagas de motos e veículos maiores
- [ ] Impedir entrada após lotação máxima
- [ ] Impedir entrada de veículos acima de 12 metros
- [ ] Aplicar corretamente a gratuidade de 15 minutos
- [ ] Calcular corretamente os valores cobrados
- [ ] Registrar placas e horários
- [ ] Exibir vagas ocupadas e disponíveis
- [ ] Gerar relatório diário de faturamento
- [ ] Aplicar multas por estacionamento irregular
- [ ] Bloquear entradas fora do horário de funcionamento

---

## 🏁 11. Considerações Finais

O QuickParking foi projetado para atender às necessidades de gerenciamento de um estacionamento de loja de conveniência, proporcionando maior controle operacional, organização das vagas e precisão na cobrança dos clientes.

A utilização das metodologias ágeis Kanban e Scrum contribuiu para o acompanhamento das atividades, organização da equipe e desenvolvimento estruturado do projeto.
