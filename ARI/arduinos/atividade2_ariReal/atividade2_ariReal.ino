#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Inicializa o display no endereço 0x27 (comum no Tinkercad) com 16 colunas e 2 linhas
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Definição dos pinos dos LEDs
const int LED_VERDE = 2;
const int LED_AMARELO = 3;
const int LED_VERMELHO = 4;

// Variável para contar os ciclos do semáforo
int contadorCiclos = 0;

void setup() {
  // Configura os pinos dos LEDs como saídas
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);

  // Inicializa o LCD e liga a luz de fundo
  lcd.init();
  lcd.backlight();
  
  // Mensagem inicial rápida
  lcd.setCursor(0, 0);
  lcd.print("Semaforo Pronto");
  delay(1500);
  lcd.clear();
}

void loop() {
  // --- FASE 1: VERDE (3 Segundos) ---
  digitalWrite(LED_VERDE, HIGH);
  digitalWrite(LED_AMARELO, LOW);
  digitalWrite(LED_VERMELHO, LOW);
  
  atualizarDisplay("Verde");
  delay(3000); // Mantém por 3 segundos

  // --- FASE 2: AMARELO (1 Segundo) ---
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_AMARELO, HIGH);
  digitalWrite(LED_VERMELHO, LOW);
  
  atualizarDisplay("Amarelo");
  delay(1000); // Mantém por 1 segundo

  // --- FASE 3: VERMELHO (3 Segundos) ---
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_AMARELO, LOW);
  digitalWrite(LED_VERMELHO, HIGH);
  
  atualizarDisplay("Vermelho");
  delay(3000); // Mantém por 3 segundos

  // --- FIM DO CICLO ---
  // O ciclo termina após o vermelho. Incrementamos o contador.
  contadorCiclos++;
}

// Função auxiliar para limpar e atualizar o texto do display
void atualizarDisplay(String corAtual) {
  lcd.clear();
  
  // Linha 1: Mostra o estado atual do semáforo
  lcd.setCursor(0, 0);
  lcd.print("Status: ");
  lcd.print(corAtual);
  
  // Linha 2: Mostra o total de ciclos completados
  lcd.setCursor(0, 1);
  lcd.print("Ciclos: ");
  lcd.print(contadorCiclos);
}