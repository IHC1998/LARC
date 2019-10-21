#include <VL53L0X.h>

#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;
VL53L0X sensor2;
VL53L0X sensor3;

void setup()
{

  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);

  delay(500);
  Wire.begin();


  Serial.begin (9600);

  //SENSOR
  pinMode(9, INPUT);
  delay(50);
  Serial.println("00");
  sensor.init(true);
  Serial.println("01");
  delay(20);
  sensor.setAddress((uint8_t)22);
  Serial.println("02");

  //SENSOR 2
  pinMode(10, INPUT);
  delay(50);
  sensor2.init(true);
  Serial.println("03");
  delay(20);
  sensor2.setAddress((uint8_t)25);
  Serial.println("04");

  //SENSOR 3
  pinMode(11, INPUT);
  delay(50);
  sensor3.init(true);
  Serial.println("05");
  delay(20);
  sensor3.setAddress((uint8_t)28);
  Serial.println("06");

  Serial.println("");
  Serial.println("addresses set");
  Serial.println("");
  Serial.println("");



  sensor.setTimeout(500);
  sensor2.setTimeout(500);
  sensor3.setTimeout(500);


}

void loop()
{
  Serial.println("__________________________________________________________________");
  Serial.println("");
  Serial.println("=================================");
  Serial.println ("I2C scanner. Scanning ...");
  byte count = 0;


  //for (byte i = 1; i < 120; i++)
  for (byte i = 1; i < 30; i++)
  {

    Wire.beginTransmission (i);
    if (Wire.endTransmission () == 0)
    {
      Serial.print ("Found address: ");
      Serial.print (i, DEC);
      Serial.print (" (0x");
      Serial.print (i, HEX);
      Serial.println (")");
      count++;
      delay (1);  // maybe unneeded?
    } // end of good response
  } // end of for loop
  Serial.println ("Done.");
  Serial.print ("Found ");
  Serial.print (count, DEC);
  Serial.println (" device(s).");
  Serial.println("=================================");


  //CHECK DISTANCES
  long DISTANCE_FWD = (sensor.readRangeSingleMillimeters());
  long DISTANCE_FLT = (sensor2.readRangeSingleMillimeters());
  long DISTANCE_FRT = (sensor3.readRangeSingleMillimeters());

  //FWD OR SENSOR
  if (sensor.timeoutOccurred())
  {
    Serial.println("_________________________________");
    Serial.print("Distance FWD (READING): ");
    Serial.println(" TIMEOUT");
    Serial.println("_________________________________");
    Serial.println("");
  }
  else
  {
    Serial.println("_________________________________");
    Serial.print("Distance FWD   (m): ");
    Serial.println(DISTANCE_FWD/1000);
    Serial.print("Distance FWD (mm): ");
    Serial.println(DISTANCE_FWD);
    Serial.println("_________________________________");
    Serial.println("");
  }

  //FLT OR SENSOR2
  if (sensor2.timeoutOccurred())
  {
    Serial.println("_________________________________");
    Serial.print("Distance FLT (READING): ");
    Serial.println(" TIMEOUT");
    Serial.println("_________________________________");
    Serial.println("");
  }
  else
  {
    Serial.println("_________________________________");
    Serial.print("Distance FLT   (m): ");
    Serial.println(DISTANCE_FLT/1000);
    Serial.print("Distance FLT (mm): ");
    Serial.println(DISTANCE_FLT);
    Serial.println("_________________________________");
    Serial.println("");
  }
  
  //FRT OR SENSOR3
  if (sensor3.timeoutOccurred())
  {
    Serial.println("_________________________________");
    Serial.print("Distance FRT (READING): ");
    Serial.println(" TIMEOUT");
    Serial.println("_________________________________");
    Serial.println("");
  }
  else
  {
    Serial.println("_________________________________");
    Serial.print("Distance FRT   (m): ");
    Serial.println(DISTANCE_FRT/1000);
    Serial.print("Distance FRTD (mm): ");
    Serial.println(DISTANCE_FRT);
    Serial.println("_________________________________");
    Serial.println("");
  }


  
  Serial.println("__________________________________________________________________");
  Serial.println();
  Serial.println();
  Serial.println();
  Serial.println();


  
  delay(2000);//can change to a lower time like 100
}
