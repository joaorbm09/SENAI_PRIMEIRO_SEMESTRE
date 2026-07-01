import sys  # Importa o módulo do sistema nativo do Python para permitir o encerramento do programa via sys.exit()

# ==========================================
# 1. ESTRUTURA DE DADOS & BANCO DE MEMÓRIA
# ==========================================

# Cria uma matriz bidimensional (5x5) para representar o mapa físico do estacionamento (25 vagas no total)
# Cada elemento da lista representa o estado de uma vaga específica
estacionamento = [
    ["[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]"],  # Fileira 0: Área Comum (Vagas Grandes)
    ["[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]"],  # Fileira 1: Área Comum (Vagas Grandes)
    ["[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]"],  # Fileira 2: Área Comum (Vagas Grandes)
    # ------------------ BOLSÃO ADAPTADO DE MOTOS ------------------
    ["[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]"],  # Fileira 3: Área Exclusiva de Motos (Vagas Pequenas)
    ["[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]", "[ Livre ]"]   # Fileira 4: Área Exclusiva de Motos (Vagas Pequenas)
]

dados_veiculos = {}        # Dicionário (tabela hash) para mapear a Placa do veículo aos seus dados (tipo, horário, vagas ocupadas)
faturamento_total = 0.0    # Variável global acumuladora do dinheiro total arrecadado no dia (número decimal)
veiculos_atendidos_dia = 0 # Variável global contadora para registrar quantos veículos pagaram e saíram no dia

# CONFIGURAÇÕES E CREDENCIAIS CONSTANTES
HORA_ABERTURA = 5          # Define o horário de abertura do estabelecimento (5h da manhã)
HORA_FECHAMENTO = 22       # Define o horário de fechamento do estabelecimento (22h da noite)
SENHA_ADMIN = "admin123"   # Senha de texto estática exigida para liberar o painel de faturamento/gerencial

# ==========================================
# 2. FUNÇÕES AUXILIARES / SINALIZAÇÃO
# ==========================================

def formatar_hora(h, m):
    """Recebe hora e minuto inteiros e retorna uma string formatada como 'HH:MM' com zeros à esquerda."""
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}"

def validar_horario(h):
    """Verifica se a hora digitada está dentro do intervalo permitido de funcionamento (retorna True ou False)."""
    return HORA_ABERTURA <= h < HORA_FECHAMENTO

def exibir_mapa_filtrado(linhas_permitidas, titulo_setor):
    """Exibe no terminal apenas as fileiras correspondentes à categoria do veículo selecionado."""
    print("\n" + "-"*55)  # Imprime uma linha estética divisória de traços
    print(f"      VAGAS DISPONÍVEIS - {titulo_setor}") # Cabeçalho com o nome do setor
    print("-"*55)
    print("            [Vaga 0]   [Vaga 1]   [Vaga 2]   [Vaga 3]   [Vaga 4]") # Legenda de colunas
    for i in range(5):  # Loop que percorre todas as 5 fileiras da matriz do estacionamento
        if i in linhas_permitidas:  # Se a fileira atual for permitida para o veículo, ela será desenhada
            print(f"Fileira {i} ->   ", end="")  # Imprime o indicador de início da linha sem pular linha
            for j in range(5):  # Loop interno que passa por cada uma das 5 vagas daquela fileira
                vaga = estacionamento[i][j]  # Pega o conteúdo atual da vaga (seja '[ Livre ]' ou '[ABC1D23]')
                print(f"{vaga:<10}", end=" ")  # Imprime a vaga alinhada à esquerda ocupando 10 espaços físicos
            print("\n")  # Pula uma linha ao final de cada fileira impressa
    print("-"*55)

def exibir_mapa_completo():
    """Gera o painel visual completo com todas as 25 vagas para a auditoria do administrador."""
    print("\n" + "="*65)  # Divisória dupla estética
    print("      PAINEL GERAL DE SINALIZAÇÃO - VISÃO ADMINISTRADOR")
    print("="*65)
    print("--- SETOR COMUM (CARRO / PICAPE / CAMINHÃO) ---")
    for i in range(3):  # Percorre estritamente as fileiras de área comum (0, 1 e 2)
        print(f"Fileira {i} -> ", end="")
        for j in range(5):
            print(f"{estacionamento[i][j]:<10}", end=" ")  # Imprime as vagas formatadas
        print("\n")
    print("--- BOLSÃO EXCLUSIVO DE MOTOS ---")
    for i in range(3, 5):  # Percorre estritamente as fileiras do bolsão de motos (3 e 4)
        print(f"Fileira {i} -> ", end="")
        for j in range(5):
            print(f"{estacionamento[i][j]:<10}", end=" ")
        print("\n")
    print("="*65)

# ==========================================
# 3. CORE DO SISTEMA (REQUISITOS FUNCIONAIS)
# ==========================================

def registrar_entrada():
    """Gerencia todo o fluxo de entrada: valida horário, cataloga o veículo, valida tamanho e aloca as vagas."""
    global dados_veiculos  # Indica ao interpretador que usará a tabela hash global declarada no início
    print("\n--- PASSO 1: QUESTIONÁRIO DO VEÍCULO ---")
    
    try:
        hora_atual = int(input("Hora atual do sistema (5-22): "))  # Lê e converte a hora da entrada para inteiro
        min_atual = int(input("Minuto atual do sistema (0-59): "))  # Lê e converte o minuto da entrada para inteiro
        if not (0 <= hora_atual <= 23 and 0 <= min_atual <= 59):  # Validação relógio matemático universal
            raise ValueError  # Força o disparo de um erro caso o usuário digite horas absurdas como 27:85
    except ValueError:
        print("[ERRO] Horário inválido!")  # Avisa o usuário sobre o erro de digitação
        return  # Cancela e sai imediatamente da função, retornando ao menu principal

    if not validar_horario(hora_atual):  # Invoca a checagem de horário comercial (5h às 22h)
        print(f"[BLOQUEADO] Estacionamento fechado! Horário: {HORA_ABERTURA:02d}h às {HORA_FECHAMENTO:02d}h.")
        return  # Bloqueia e encerra o fluxo se o pátio estiver fechado

    placa = input("Digite a placa do veículo: ").strip().upper()  # Remove espaços extras e põe tudo em maiúsculo
    if not placa:  # Verifica se o operador simplesmente apertou Enter sem digitar nada
        print("[ERRO] Placa inválida!")
        return
    if placa in dados_veiculos:  # Consulta rápida no dicionário para ver se o veículo já está ocupando o pátio
        print("[ALERTA] Este veículo já está estacionado!")
        return

    print("Selecione o tipo do veículo:")
    print("1 - Carro\n2 - Picape\n3 - Caminhão\n4 - Moto")
    opcao_tipo = input("Opção: ").strip()  # Captura a escolha do tipo do veículo

    vagas_necessarias = 1  # Define o padrão: por padrão qualquer veículo ocupa exatamente 1 vaga física
    
    if opcao_tipo in ['1', '2', '3']:  # Agrupamento de categorias que utilizam o Setor Comum (Vagas Grandes)
        linhas_busca = [0, 1, 2]       # Delimita a busca apenas para as linhas 0, 1 e 2 da matriz
        titulo_setor = "SETOR CARROS / CAMINHÕES"
        tipo = "Carro" if opcao_tipo == '1' else "Picape" if opcao_tipo == '2' else "Caminhão"  # Estrutura ternária
        
        if tipo == "Caminhão":  # Se for caminhão, inicia sub-questionário físico obrigatório
            try:
                comprimento = float(input("Digite o comprimento do caminhão (metros): "))  # Converte tamanho para decimal
                largura = float(input("Digite a largura do caminhão (metros): "))          # Converte largura para decimal
                if comprimento > 12.0 or largura > 2.0:  # Regra de restrição física total do pátio de manobras
                    print("[BARRA-LO] Proibido! Caminhão excede o tamanho limite do pátio (12m x 2m).")
                    return  # Bloqueia a entrada do veículo gigante
                
                if comprimento > 6.0:  # Ativação da regra de negócio de ocupação sequencial dupla
                    vagas_necessarias = 2  # Altera a necessidade para duas vagas consecutivas
                    print("[AVISO GERENCIAL] Caminhão longo detectado! Ocupará 2 vagas consecutivas na mesma fileira.")
            except ValueError:
                print("[ERRO] Tamanho inválido.")
                return
    elif opcao_tipo == '4':  # Categoria Moto
        linhas_busca = [3, 4]  # Delimita o estacionamento apenas para o Bolsão de Motos (linhas 3 e 4)
        titulo_setor = "BOLSÃO DE MOTOS"
        tipo = "Moto"
    else:
        print("[ERRO] Opção inválida.")
        return

    # Loop de Escolha de Vagas Interativo (Garante que o usuário só saia daqui ao digitar uma vaga livre e válida)
    while True:
        exibir_mapa_filtrado(linhas_busca, titulo_setor)  # Mostra o mapa customizado para o motorista
        print("--- PASSO 2: ESCOLHA SUA VAGA ---")
        
        try:
            if vagas_necessarias == 2:
                print("Como seu caminhão ocupa 2 vagas, digite a PRIMEIRA delas. A vaga seguinte à direita será reservada.")
            
            escolha_fila = int(input(f"Escolha a Fileira ({', '.join(map(str, linhas_busca))}): "))  # Captura o índice da fileira
            escolha_vaga = int(input("Escolha o número da Vaga (0 a 4): "))                         # Captura o índice da vaga
            
            # Valida as fronteiras da matriz impedindo estouro de memória (IndexError)
            if escolha_fila not in linhas_busca or not (0 <= escolha_vaga <= 4):
                print("\n[ERRO] Posição inválida para a sua categoria! Tente novamente.")
                continue  # Reinicia o loop de digitação de vagas
            
            # PROTEÇÃO DO CAMINHÃO DUPLO: Se escolher vaga 4, ele tentaria pegar a 4 e a 5 (que não existe)
            if vagas_necessarias == 2 and escolha_vaga >= 4:
                print("\n[ERRO] Caminhões longos não podem escolher a última vaga (Vaga 4) de uma fileira!")
                continue  # Reinicia o loop bloqueando o estouro do índice
                
            # Fluxo de verificação de disponibilidade real das vagas
            if vagas_necessarias == 1:
                if estacionamento[escolha_fila][escolha_vaga] != "[ Livre ]":  # Se a vaga contiver uma placa antiga
                    print("\n[VAGA OCUPADA] Essa vaga já está sendo usada. Escolha outra.")
                    continue  # Força nova escolha
                vagas_alocar = [(escolha_fila, escolha_vaga)]  # Grava a tupla com as coordenadas da vaga única
            else:
                # Checagem dupla simultânea: verifica a vaga escolhida E a imediatamente ao lado (escolha_vaga + 1)
                if estacionamento[escolha_fila][escolha_vaga] != "[ Livre ]" or estacionamento[escolha_fila][escolha_vaga + 1] != "[ Livre ]":
                    print("\n[VAGAS OCUPADAS] O caminhão precisa de duas vagas seguidas livres (esta e a próxima)! Tente outra.")
                    continue  # Força nova escolha caso alguma das duas esteja ocupada
                vagas_alocar = [(escolha_fila, escolha_vaga), (escolha_fila, escolha_vaga + 1)]  # Grava as duas coordenadas
                
            break  # Sucesso total em todas as validações, quebra o loop infinito de escolha de vaga
                
        except ValueError:
            print("\n[ERRO] Digite valores numéricos válidos!")
            continue  # Trata caso o usuário digite uma letra nos inputs numéricos das coordenadas

    # Alocação estruturada na Matriz de dados do estacionamento físico
    for f, v in vagas_alocar:
        estacionamento[f][v] = f"[{placa}]"  # Substitui o texto '[ Livre ]' pela tag contendo a placa do veículo
        
    # Salva o estado atual e metadados completos do veículo na memória ativa do sistema
    dados_veiculos[placa] = {
        "tipo": tipo,
        "hora_entrada": hora_atual,
        "min_entrada": min_atual,
        "vagas_ocupadas": vagas_alocar  # Armazena a lista de tuplas para sabermos quais pontos limpar na saída
    }
    
    # Exibe feedbacks customizados no console para o operador dependendo da envergadura do veículo
    if vagas_necessarias == 1:
        print(f"\n[SUCESSO] {tipo} [{placa}] estacionado na Fileira {escolha_fila}, Vaga {escolha_vaga}!")
    else:
        print(f"\n[SUCESSO] Caminhão [{placa}] estacionado ocupando as Vagas {escolha_vaga} e {escolha_vaga + 1} da Fileira {escolha_fila}!")


def registrar_saida():
    """Calcula o tempo de permanência considerando mudanças de dia, computa taxas, cobra e limpa a vaga física."""
    global faturamento_total, veiculos_atendidos_dia, dados_veiculos  # Carrega o acesso às variáveis globais financeiras
    print("\n--- RF02/RF03 - REGISTRAR SAÍDA E COBRANÇA ---")
    placa = input("Digite a placa do veículo para saída: ").strip().upper()
    
    if placa not in dados_veiculos:  # Valida se a placa de fato existe no pátio ativo
        print("[ERRO] Veículo não encontrado no pátio ativo.")
        return  # Aborta se o veículo nunca deu entrada

    veiculo = dados_veiculos[placa]  # Recupera o dicionário de informações interna daquele veículo específico
    print(f"Veículo localizado: {veiculo['tipo']} | Entrada: {formatar_hora(veiculo['hora_entrada'], veiculo['min_entrada'])}")
    
    try:
        hora_saida = int(input("Hora atual de saída (5-22): "))   # Registra a hora da saída
        min_saida = int(input("Minuto atual de saída (0-59): "))  # Registra o minuto da saída
        if not (0 <= hora_saida <= 23 and 0 <= min_saida <= 59):  # Valida o formato horário universal
            raise ValueError
    except ValueError:
        print("[ERRO] Horário inválido!")
        return

    # Algoritmo de Linha do Tempo: Converte todo o tempo de entrada e saída para minutos absolutos
    minutos_entrada = (veiculo['hora_entrada'] * 60) + veiculo['min_entrada']
    minutos_saida = (hora_saida * 60) + min_saida
    
    # ARITMÉTICA MODULAR (% 1440): Resolve nativamente o problema de virada de dia (ex: entrar 22h e sair 06h do outro dia)
    # 1440 representa a quantidade de minutos totais contidos em 24 horas completas.
    tempo_permanencia = (minutos_saida - minutos_entrada) % 1440
    
    if tempo_permanencia == 0:
        tempo_permanencia = 1  # Segurança matemática: se entrou e saiu no exato minuto, cobra 1 minuto

    valor_total_pago = 0.0  # Inicializa a variável do preço
    
    if tempo_permanencia <= 15:  # Regra de tolerância / carência legal estabelecida
        print(f"[CARÊNCIA] Tempo total de {tempo_permanencia} min. Saída Gratuita.")
    else:
        # Algoritmo de Arredondamento para Cima: converte os minutos fracionados em blocos de horas cheias
        # Exemplo: 16 minutos vira 1 hora de cobrança. 61 minutos vira 2 horas de cobrança.
        horas_cobranca = (tempo_permanencia - 1) // 60 + 1
        
        if horas_cobranca <= 1:
            tarifa_base = 10.0  # Primeira hora fixa possui valor integral de R$ 10.00
        else:
            tarifa_base = 10.0 + (horas_cobranca - 1) * 5.0  # Horas adicionais subsequentes custam R$ 5.00 cada
            
        # REGRA DE ESPAÇO: Se o veículo ocupou duas vagas (caminhão longo), o valor da tarifa base é dobrado
        if len(veiculo['vagas_ocupadas']) == 2:
            valor_total_pago = tarifa_base * 2
            print(f"[PRESIZO] Espaço Duplo Utilizado: Valor multiplicado por 2.")
        else:
            valor_total_pago = tarifa_base  # Carros, Motos e Picapes pagam a tarifa padrão de 1 vaga

    # Emissão finalizada do Extrato/Recibo no console
    print("\n" + "-"*40)
    print("           RECIBO DE SAÍDA")
    print("-"*40)
    print(f"Placa do Veículo : {placa}")
    print(f"Permanência      : {tempo_permanencia} minutos ({horas_cobranca}h cobradas)")
    print(f"VALOR TOTAL REAL : R$ {valor_total_pago:.2f}")
    print("-"*40)

    confirmacao = input("Confirmar pagamento e liberar vaga(s)? (S/N): ").strip().upper()
    if confirmacao == 'S':
        # Varre as coordenadas salvas e limpa TODAS as vagas associadas ao veículo, tornando-as '[ Livre ]'
        for f, v in veiculo['vagas_ocupadas']:
            estacionamento[f][v] = "[ Livre ]"
            
        faturamento_total += valor_total_pago       # Adiciona o dinheiro pago ao cofre/caixa bruto do dia
        veiculos_atendidos_dia += 1                 # Incrementa o número de atendimentos concluídos com sucesso
        del dados_veiculos[placa]                   # Deleta o registro do carro do dicionário de pátio ativo
        print("[SUCESSO] Espaço físico liberado e caixa atualizado!")
    else:
        print("[SAÍDA CANCELADA] A vaga permanece ocupada até a confirmação do pagamento.")


def area_administrative():
    """Restringe o acesso por senha e exibe relatórios financeiros consolidados de auditoria interna."""
    senha = input("\nDigite a senha de administrador: ").strip()
    if senha != SENHA_ADMIN:  # Bloqueio de segurança comparativo de strings
        print("[ACESSO NEGADO] Senha incorreta!")
        return  # Ejeta o usuário intruso de volta para o menu inicial

    while True:  # Loop do Submenu Administrativo
        print("\n--- PAINEL ADMINISTRATIVO RESTRITO ---")
        print("1 - Visualizar Mapa Geral Completo (Sinalização)")
        print("2 - Relatório de Faturamento do Dia")
        print("0 - Voltar ao Menu Principal")
        
        op = input("Selecione o comando: ").strip()
        if op == '1':
            exibir_mapa_completo()  # Executa a renderização geral do grid de 25 vagas
        elif op == '2':
            # Exibe o sumário financeiro consolidado do dia corrente
            print("\n" + "*"*45)
            print(f"Total de Veículos Encerrados  : {veiculos_atendidos_dia}")
            print(f"Faturamento Arrecadado Bruto  : R$ {faturamento_total:.2f}")
            print(f"Veículos no Pátio Atualmente  : {len(dados_veiculos)}") # Conta o tamanho atual do dicionário
            print("*"*45)
        elif op == '0':
            break  # Quebra o loop interno administrativo e retorna ao menu geral
        else:
            print("[ERRO] Opção inválida.")


def main():
    """Função mestre que atua como o motor do programa, controlando o menu de opções principal."""
    while True:  # Loop perpétuo de execução do software
        print("\n=== QUICKPARKING v4.0 (MATRIX TRUCK-SIZE) ===")
        print("1 - Entrada de Veículo (Questionário + Escolha de Vaga)")
        print("2 - Saída de Veículo / Pagamento")
        print("3 - Área Administrativa (Requer Senha)")
        print("0 - Fechar Sistema")
        
        opcao = input("Selecione a opção: ").strip()
        
        if opcao == '1':
            registrar_entrada()  # Desvia a execução para a rotina de entrada
        elif opcao == '2':
            registrar_saida()    # Desvia a execução para a rotina de saída/pagamento
        elif opcao == '3':
            area_administrative() # Desvia a execução para a zona gerencial protegida
        elif opcao == '0':
            print("Encerrando o QuickParking.")
            sys.exit()  # Finaliza o processo do Python e desliga o script de forma limpa
        else:
            print("[ERRO] Opção inválida!")  # Trata erros de digitação no menu principal

# Cláusula idiomática do Python que garante que o programa só rodará se executado diretamente pelo terminal
if __name__ == "__main__":
    main()  # Dispara a função principal para iniciar o sistema
