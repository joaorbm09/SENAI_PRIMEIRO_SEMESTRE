// Definição dos pinos onde cada LED do semáforo está conectado
int vermelho = 2; // LED Vermelho conectado ao pino digital 2
int amarelo = 3;  // LED Amarelo conectado ao pino digital 3
int verde = 4;    // LED Verde conectado ao pino digital 4

void setup()
{
  //  todos os pinos dos LEDs como saídas de sinal (OUTPUT)
  pinMode(vermelho, OUTPUT);
  pinMode(amarelo, OUTPUT);
  pinMode(verde, OUTPUT);
}

void loop()
{
  //  AMARELO 
  digitalWrite(amarelo, HIGH); // Acende o LED Amarelo
  digitalWrite(vermelho, LOW); // Garante que o Vermelho está apagado
  digitalWrite(verde, LOW);    // Garante que o Verde está apagado
  
  delay(2000); // O Amarelo fica aceso por 2 segundos (2000 milissegundos)

  //  VERMELHO 
  digitalWrite(amarelo, LOW);   // Apaga o LED Amarelo
  digitalWrite(vermelho, HIGH); // Acende o LED Vermelho (os carros devem parar)
  
  
  delay(5000); // Mantém o Vermelho aceso por 5 segundos (5000 milissegundos)

  //   VERDE 
  digitalWrite(vermelho, LOW); // Apaga o LED Vermelho
  digitalWrite(verde, HIGH);   // Acende o LED Verde (os carros podem seguir)
  
  
  delay(5000); // Mantém o Verde aceso por 5 segundos (5000 milissegundos)
  
  // Ao chegar ao fim do loop(), o Arduino volta automaticamente para o topo,
  // ou seja, vai apagar o Verde e acender o Amarelo (Fase 1), recomeçando o ciclo.
}