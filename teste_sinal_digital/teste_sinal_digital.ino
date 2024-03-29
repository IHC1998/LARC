//Declaração das constantes
const int led = 13;   //constante led refere-se ao pino digital 8.
const int rasp = 2; //constante botão refere-se ao pino digital 2.
 
//Variável que conterá os estados do botão (0 LOW, 1 HIGH).
int estadoRasp = 0;
 
//Método setup, executado uma vez ao ligar o Arduino.
void setup() {
  pinMode(led,OUTPUT);  //Definindo pino digital 8 como de saída.
  pinMode(rasp,INPUT); //Definindo pino digital 2 como de entrada. 
}
 
//Método loop, executado enquanto o Arduino estiver ligado.
void loop() {  
  //Lendo o estado do pino 2, constante botao, e atribuindo 
  //o resultado a variável estadoBotao.
  estadoRasp = digitalRead(rasp);          
   
  //Verificando o estado do botão para definir se acenderá ou
  //apagará o led.  
  if (estadoRasp == HIGH) {
    digitalWrite(led,HIGH); //Botão pressionado, acende o led.
  } else {
    digitalWrite(led,LOW);  //Botão não pressionado, apaga o led.    
  }       
}
