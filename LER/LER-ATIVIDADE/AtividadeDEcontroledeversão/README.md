# Sistema de Gerenciamento de Reservas de Hotel

## 1. Introdução 

### 1.1 Propósito 
este documento especifica os requisitos funcioanis de um sistema de reserva de hoteis

### 1.2 Escopo
O sistema permitirá que usuários organizem e acompanhem suas reservas e sisstema de prazos. 

### 1.3 Acrônimos - Definição
-**RF**: Requisitos funionais
-**SGR**: sistema de gerenciamento de reservas

### 1.4 Referências

## 2. Descrição Geral
O SGR será uma aplicação web responsiva com sincronização em nuvens.

###2.2 Funções Principais

- Reserva de quartos 
- Organização de quartos disponiveis
- Sistema de notificação
- Relatórios de preços
- 
## 3. Requisitos Específicos

### 3.1 Requisto Funcional 

#### RF-010: Os usuários devem ser capazes de selcionar suas reservas de quartos do hotel

**Descrição**: O sistema deve permitir que usuarios realizem reservas de quartos com antecedência mínima de 24 horas e máxima de 6 meses
**Prioridade**: alta
**Versão**: 1.0 
**Data**: 2026-01-01
**Rastreabilidade**: o rastreio será de forma cadastro e login do usuário na plataforma.

---

**Critérios de aceitação**:

- [ ] usuario pode fazer uma reserva minima de 24 horas
- [ ] usuarioas podem fazer uma reserva de antecedência de até no maximo de 6 meses
- [ ] visualização de quartos disponiveis e indisponiveis 

**depndências**: RF-001

- [ ] o sitemas deve estar ligado com o login e cadastro dos usuarios
- [ ] o sistema deve ter ligação com banco de dados( para armazenamento das contas e de aprovações bancarias)
- [ ] e validação das datas de reservas

---

## 4. Controle de Versão
| VErsão | Data | Autor | Modificação |
|--------|------|-------|-------------|
| 1.0    | 2026-01-01 | João Wictor | Versão inicial de documento |
### 4.1 Histórico de Alterações 

| VErsão | Data | Autor | Modificação |
|--------|------|-------|-------------|
| 1.1    | 2026-0-10 | João Wictor | Criação do documento |

## 5. Aprovação 
| Alteração | Data | Autor | Aprovador |
| -   | - | - | - | 
| 1.0  | 2026-01-01 | João Wictor | Stakeholder | 
