#include <Wire.h>
#include <VL53L0X.h>

#define qtdMedia 20

VL53L0X sensor;
VL53L0X sensor2;
VL53L0X sensor3;
int inf_e = 8;
int inf_m = 12;
int inf_d = 13;

float mediaLeft, mediaMiddle, mediaRight;

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

  sensor.setTimeout(20);
  sensor2.setTimeout(20);
  sensor3.setTimeout(20);
}

void loop() {
  //DISTANCE_L = Distância sensor da esquerda / DISTANCE_R = Distância sensor da direita
  //DISTANCE_M = Distânica sensor do meio
  mediaLeft = 0; 
  mediaMiddle = 0;
  mediaRight = 0;
      
  for(int j=0; j<qtdMedia; j++){
      mediaLeft += sensor.readRangeSingleMillimeters(); 
      mediaMiddle += sensor2.readRangeSingleMillimeters();
      mediaRight += sensor3.readRangeSingleMillimeters();
  }
  
  mediaLeft = mediaLeft/qtdMedia;
  mediaMiddle = mediaMiddle/qtdMedia;
  mediaRight = mediaRight/qtdMedia;
  
  Serial.println(mediaLeft);
  Serial.println(mediaMiddle);
  Serial.println(mediaRight); 
}
