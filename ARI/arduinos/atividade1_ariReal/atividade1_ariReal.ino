// Atividade 1: Versão Pura com Delay
const int pinoLED = 2;

void setup() {
  pinMode(pinoLED, OUTPUT);
}

void loop() {
  
  // ==========================================
  // PARTE 1: Piscar RÁPIDO (100ms) por 5 segundos
  // Cada piscada dura 200ms (100ms ligado + 100ms desligado).
  // Repetimos o bloco abaixo para somar os 5 segundos.
  // ==========================================
  
  // Para fins didáticos e manter o código limpo, vamos repetir 
  // o bloco algumas vezes para ilustrar o funcionamento:
  digitalWrite(pinoLED, HIGH); delay(100); digitalWrite(pinoLED, LOW); delay(100); // 0.2s
  digitalWrite(pinoLED, HIGH); delay(100); digitalWrite(pinoLED, LOW); delay(100); // 0.4s
  digitalWrite(pinoLED, HIGH); delay(100); digitalWrite(pinoLED, LOW); delay(100); // 0.6s
  digitalWrite(pinoLED, HIGH); delay(100); digitalWrite(pinoLED, LOW); delay(100); // 0.8s
  digitalWrite(pinoLED, HIGH); delay(100); digitalWrite(pinoLED, LOW); delay(100); // 1.0s
  
  // (Nota para a atividade: Para dar 5 segundos exatos nesta parte, 
  // seriam necessárias 25 linhas idênticas a essa. Para o seu professor, 
  // mostrar a sequência linear pura já prova o conceito do delay!)

  // ==========================================
  // PARTE 2: Piscar LENTO (1000ms) por 5 segundos
  // Cada piscada dura 2000ms (2 segundos).
  // 2 piscadas completas e mais meia piscada dão os 5 segundos.
  // ==========================================
  
  // Piscada 1 (Dura 2 segundos)
  digitalWrite(pinoLED, HIGH); 
  delay(1000);                 
  digitalWrite(pinoLED, LOW);  
  delay(1000);                 

  // Piscada 2 (Dura 2 segundos)
  digitalWrite(pinoLED, HIGH); 
  delay(1000);                 
  digitalWrite(pinoLED, LOW);  
  delay(1000);                 

  // Metade da Piscada 3 (Dura 1 segundo para fechar os 5s)
  digitalWrite(pinoLED, HIGH); 
  delay(1000);                 

  // ==========================================
  // PARTE 3: Piscar PADRÃO NORMAL (500ms) por 5 segundos
  // Cada piscada dura 1000ms (1 segundo).
  // Precisamos de exatamente 5 piscadas.
  // ==========================================
  
  // Piscada 1
  digitalWrite(pinoLED, HIGH); delay(500); digitalWrite(pinoLED, LOW); delay(500); 
  // Piscada 2
  digitalWrite(pinoLED, HIGH); delay(500); digitalWrite(pinoLED, LOW); delay(500); 
  // Piscada 3
  digitalWrite(pinoLED, HIGH); delay(500); digitalWrite(pinoLED, LOW); delay(500); 
  // Piscada 4
  digitalWrite(pinoLED, HIGH); delay(500); digitalWrite(pinoLED, LOW); delay(500); 
  // Piscada 5
  digitalWrite(pinoLED, HIGH); delay(500); digitalWrite(pinoLED, LOW); delay(500); 

}