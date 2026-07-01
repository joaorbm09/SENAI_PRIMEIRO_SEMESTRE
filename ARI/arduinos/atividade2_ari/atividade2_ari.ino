// Definição dos pinos para o Semáforo 1 (Via 1)
int VM1 = 10; // Vermelho 1 no pino digital 10
int AM1 = 9;  // Amarelo 1 no pino digital 9
int VE1 = 8;  // Verde 1 no pino digital 8

// Definição dos pinos para o Semáforo 2 (Via 2)
int VM2 = 7;  // Vermelho 2 no pino digital 7
int AM2 = 6;  // Amarelo 2 no pino digital 6
int VE2 = 5;  // Verde 2 no pino digital 5

void setup()
{
  // Configura todos os pinos dos LEDs como saídas de sinal (OUTPUT)
  pinMode(VM1, OUTPUT);
  pinMode(AM1, OUTPUT);
  pinMode(VE1, OUTPUT);
  pinMode(VM2, OUTPUT);
  pinMode(AM2, OUTPUT);
  pinMode(VE2, OUTPUT);

  // --- ESTADO INICIAL DO CRUZAMENTO ---
  // Semáforo 1 inicia Aberto (Verde)
  digitalWrite(VE1, HIGH);
  digitalWrite(AM1, LOW);
  digitalWrite(VM1, LOW);
  
  // Semáforo 2 inicia Fechado (Vermelho)
  digitalWrite(VE2, LOW);
  digitalWrite(AM2, LOW);
  digitalWrite(VM2, HIGH);
  
  delay(5000); // Mantém esse estado inicial por 5 segundos
}

void loop()
{
  //  Se o Semáforo 1 está Verde, é hora de ir para o Amarelo
  if (digitalRead(VE1) == HIGH) 
  {
    digitalWrite(VE1, LOW);   // Apaga o Verde 1
    digitalWrite(AM1, HIGH);  // Acende o Amarelo 1
    delay(2000);              // Aguarda 2 segundos (tempo do amarelo)
  }
  
   // Se o Semáforo 1 está Amarelo, ele deve fechar e o Semáforo 2 abrir
  else if (digitalRead(AM1) == HIGH) 
  {
    digitalWrite(AM1, LOW);   // Apaga o Amarelo 1
    digitalWrite(VM1, HIGH);  // Acende o Vermelho 1 (Fecha a Via 1)
    
    digitalWrite(VM2, LOW);   // Apaga o Vermelho 2
    digitalWrite(VE2, HIGH);  // Acende o Verde 2 (Abre a Via 2)
    delay(5000);              // Mantém os carros passando na Via 2 por 5 segundos
  }
  
  // Se o Semáforo 2 está Verde, é hora de ir para o Amarelo dele
  else if (digitalRead(VE2) == HIGH) 
  {
    digitalWrite(VE2, LOW);   // Apaga o Verde 2
    digitalWrite(AM2, HIGH);  // Acende o Amarelo 2
    delay(2000);              // Aguarda 2 segundos (tempo do amarelo)
  }
  
  //  Se o Amarelo 2 estava aceso (última possibilidade restante)
  else 
  {
    digitalWrite(AM2, LOW);   // Apaga o Amarelo 2
    digitalWrite(VM2, HIGH);  // Acende o Vermelho 2 (Fecha a Via 2)
    
    digitalWrite(VM1, LOW);   // Apaga o Vermelho 1
    digitalWrite(VE1, HIGH);  // Acende o Verde 1 (Reabre a Via 1)
    delay(5000);              // Mantém os carros passando na Via 1 por 5 segundos
  }
}