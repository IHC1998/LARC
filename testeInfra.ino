#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;
VL53L0X sensor2;
VL53L0X sensor3;
int inf_e = 8;
int inf_m = 12;
int inf_d = 13;

unsigned long previousMillis;
long delayEnvio = 50; //Tempo em ms do intervalo a ser executado

void setup() {
  // put your setup code here, to run once:.
  Serial.begin(9600);
  pinMode(inf_e, OUTPUT);
  pinMode(inf_m, OUTPUT);
  pinMode(inf_d, OUTPUT);
  digitalWrite(inf_e, LOW);
  digitalWrite(inf_m, LOW);
  digitalWrite(inf_d, LOW);
  delay(100);
  Wire.begin();

  //SENSOR 1
  pinMode(inf_e, INPUT);
  sensor.init(true);
  sensor.setAddress((uint8_t)22);

  //SENSOR 2
  pinMode(inf_m, INPUT);
  sensor2.init(true);
 sensor2.setAddress((uint8_t)25);

  //SENSOR 3
 pinMode(inf_d, INPUT);
 sensor3.init(true);
  sensor3.setAddress((uint8_t)28);

  sensor.setTimeout(50);
  sensor2.setTimeout(50);
  sensor3.setTimeout(50);
}

void loop() {
  //DISTANCE_L = Distância sensor da esquerda / DISTANCE_R = Distância sensor da direita
  //DISTANCE_M = Distânica sensor do meio
  
  float DISTANCE_L = (sensor.readRangeSingleMillimeters());
  float DISTANCE_R = (sensor2.readRangeSingleMillimeters());
  float DISTANCE_M = (sensor3.readRangeSingleMillimeters());

  Serial.println(DISTANCE_L);
  Serial.println(DISTANCE_R);
  Serial.println(DISTANCE_M); 
  delay(50);




  
}
