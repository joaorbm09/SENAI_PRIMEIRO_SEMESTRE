//importando a biblioteca Bluetooh
#include "BluetoothSerial.h"

//criando o objeto SerialBT
BluetoothSerial SerialBT;


// Declarando os pinos em uma variavel
const int LED1 = 19;
const int LED2 = 18;
const int LED3 = 17;
const int LED4 = 16;
const int LED5 = 4;
const int LED6 = 15;

// DEcalrar as variaveis
char comando;


// nos precisimos inicializar os pinos e componentes
void setup(){
  pinMode(LED1,OUTPUT); // declarando como saidas
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  pinMode(LED4,OUTPUT);
  pinMode(LED5,OUTPUT);
  pinMode(LED6,OUTPUT);
  SerialBT.begin("MATOS"); // nomeando o nosso dispositivo
}

// precisamos de uma função que irá se repetir
void loop(){
  if(SerialBT.available()){
    comando = SerialBT.read();
    if (comando == 'l'){  
      digitalWrite(LED1,HIGH); // o led ira acender
      digitalWrite(LED2,HIGH);
      digitalWrite(LED3,HIGH);
      digitalWrite(LED4,HIGH);
      digitalWrite(LED5,HIGH);
      digitalWrite(LED6,HIGH);
      SerialBT.println("LEDs ligados");
    }

    if (comando == 'k'){
      digitalWrite(LED1,LOW); // o led ira acender
      digitalWrite(LED2,LOW);
      digitalWrite(LED3,LOW);
      digitalWrite(LED4,LOW);
      digitalWrite(LED5,LOW);
      digitalWrite(LED6,LOW);
      SerialBT.println("LEDs Desligados");

    }
  } 
}









