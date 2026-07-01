# Relatório de Exercícios Python - S1_R3 - AT1_LOPAL

## Descrição Geral
Este repositório contém 11 exercícios práticos em Python, desenvolvidos para consolidar conceitos fundamentais de programação, incluindo estruturas de controle, funções, manipulação de dados e validação de entrada.

---

## Exercícios

### **1 - Exercicio.py** - Classificação de Números Pares e Ímpares
**Objetivo:** Identificar e classificar números como pares ou ímpares.

**Funcionalidade:**
- Itera de 0 a 100
- Verifica se cada número é par (divisível por 2) ou ímpar
- Exibe a classificação de cada número

**Conceitos:** Loops (`for`), operador módulo (`%`), estruturas condicionais (`if/else`)

---

###  **2 - Exercicio.py** - Maior e Menor Entre Três Números
**Objetivo:** Encontrar o maior e menor valor entre três números informados.

**Funcionalidade:**
- Solicita 3 números ao usuário
- Armazena em uma lista e ordena
- Exibe o maior e o menor número

**Conceitos:** Entrada de dados, listas, métodos de lista (`sort()`), indexação

---

###  **3 - Exercicio.py** - Escada com Letras do Nome
**Objetivo:** Criar uma visualização em forma de escada usando as letras do nome.

**Funcionalidade:**
- Solicita o nome do usuário
- Constrói progressivamente a escada, adicionando uma letra por linha
- Exibe cada linha incrementada

**Conceitos:** Loops, concatenação de strings, iteração sobre caracteres

---

###  **4 - Exercicio.py** - Série de Fibonacci
**Objetivo:** Gerar uma sequência de Fibonacci até um número de termos especificado.

**Funcionalidade:**
- Solicita quantos termos deseja gerar
- Valida se o número é maior que 0
- Calcula e exibe a série de Fibonacci
- Usa troca simultânea de variáveis (`a, b = b, a+b`)

**Conceitos:** Loops, validação de entrada, listas, algoritmos matemáticos

---

###  **5 - Exercicio.py** - Cadastro com Validação de Dados
**Objetivo:** Coletar e validar informações do usuário com múltiplas verificações.

**Funcionalidade:**
- Coleta dados: nome, idade, salário, sexo, estado civil
- Valida cada campo:
  - **Nome:** deve ter mais de 3 caracteres
  - **Idade:** deve estar entre 0 e 150 anos
  - **Salário:** deve ser maior que 0
  - **Sexo:** aceita 'f' ou 'm'
  - **Estado Civil:** aceita 's', 'c', 'v' ou 'd'
- Exibe todos os dados validados

**Conceitos:** Loops de validação, entrada de dados, estruturas condicionais complexas, `.lower()`

---

###  **6 - Exercicio.py** - Verificação de Números Primos
**Objetivo:** Determinar se um número é primo.

**Funcionalidade:**
- Solicita um número ao usuário
- Conta quantos divisores o número possui
- Um número é primo se tem exatamente 2 divisores (1 e ele mesmo)
- Exibe se é primo ou não

**Conceitos:** Loops, operador módulo, contadores, lógica matemática

---

###  **7 - Exercicio.py** - Cálculo de Fatorial
**Objetivo:** Calcular o fatorial de um número.

**Funcionalidade:**
- Solicita um número ao usuário
- Calcula o fatorial multiplicando todos os números de n até 1
- Exibe a operação completa e o resultado

**Conceitos:** Loops (decrescentes), acumuladores, fatoração matemática

---

###  **8 - Exercicio.py** - Operações com Listas
**Objetivo:** Demonstrar operações fundamentais com listas.

**Funcionalidade:**
- Define uma lista pré-preenchida: [5, 7, 2, 9, 4, 1, 3]
- Calcula tamanho, maior, menor e soma
- Ordena em forma crescente
- Ordena em forma decrescente
- Exibe todos os resultados

**Conceitos:** Listas, funções embutidas (`len()`, `max()`, `min()`, `sum()`), métodos de lista (`sort()`, `reverse()`)

---

###  **9 - Exercicio.py** - Tabela de Preços de Produtos
**Objetivo:** Exibir uma tabela organizada de produtos e preços.

**Funcionalidade:**
- Utiliza um dicionário para armazenar produtos e preços
- Usa `zip()` para emparelhar produtos com preços
- Formata a saída de forma legível em colunas
- Exibe a tabela organizada

**Conceitos:** Dicionários, `zip()`, formatação de strings, iteração

---

###  **10 - Exercicio.py** - Verificação de Senha
**Objetivo:** Validar uma senha com múltiplas tentativas.

**Funcionalidade:**
- Solicita uma senha ao usuário
- Valida contra a senha correta (676767)
- Permite tentativas contínuas até acertar
- Exibe "Acesso liberado" quando correto

**Conceitos:** Loops de validação, condicionais, entrada de dados

---

###  **11 - Exercicio.py** - Tabuada de um Número
**Objetivo:** Gerar a tabuada de multiplicação de um número.

**Funcionalidade:**
- Solicita um número entre 1 e 10
- Calcula e exibe a tabuada (multiplicações de 1 a 10)
- Formata a saída de forma clara

**Conceitos:** Loops, entrada de dados, operações matemáticas, formatação de saída

---

##  Resumo de Conceitos Abordados

| Conceito | Exercícios |
|----------|-----------|
| Loops (for/while) | 1, 3, 4, 5, 6, 7, 8, 11 |
| Estruturas Condicionais (if/else) | 1, 2, 4, 5, 6, 10 |
| Listas | 2, 4, 8 |
| Dicionários | 9 |
| Validação de Entrada | 5, 10 |
| Funções Embutidas | 2, 8, 9 |
| Strings e Caracteres | 3, 5 |
| Operadores Matemáticos | 6, 7, 11 |
| Algoritmos Matemáticos | 4, 6, 7 |

---

##  Como Executar

Para executar qualquer um dos exercícios, use:

```bash
python "nome_do_exercicio.py"
```

Exemplo:
```bash
python "1 - Exercicio.py"
python "5 - Exercicio.py"
```


