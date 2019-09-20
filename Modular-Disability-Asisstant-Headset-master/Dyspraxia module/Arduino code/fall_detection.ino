#include<Wire.h>
#include "arduinoFFT.h"
const int MPU = 0x68;
void setup() {
  pinMode(8,OUTPUT);
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200);
  digitalWrite(8, LOW);
}

int old_vals[6];
int old_delta[6];
int double_delta[6];

void loop()
{
  {
    Wire.beginTransmission(MPU);
    Wire.write(0x3B);
    Wire.endTransmission(false);
    Wire.requestFrom(MPU, 12, true);
    for (int i = 0; i < 6; i++)
    {
      int tmp2 = Wire.read() << 8 | Wire.read();
      int tmp1 = tmp2 - old_vals[i]; // First Derivative
      double_delta[i] = tmp1 - old_delta[i];   // Second Derivative

      //Serial.print(double_delta[i]); Serial.print("\t");      //to print in the serial plotter
      if (double_delta[i] > 31000)
      {
        Serial.print("accident");
        digitalWrite(8, HIGH);
        delay(2000);
        digitalWrite(8, LOW);
        //delay(5000);
      }
      old_delta[i] = tmp1;//new_delta[i];
      old_vals[i] = tmp2;
    }
    Serial.println();
    delay(1);
  }
}
